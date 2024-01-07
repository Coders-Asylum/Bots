using Xunit;
using Microsoft.Extensions.Logging;
using Moq;
using Bot.Exceptions;

namespace Tests.Src
{
    public class AppExceptionTests
    {
        private readonly Mock<ILogger> _mockLogger;

        public AppExceptionTests()
        {
            _mockLogger = new Mock<ILogger>();
        }

        [Fact]
        public void AppException_ModifiesMessage_WithException()
        {
            // Arrange
            var code = "TEST_CODE";
            var message = "Test message";
            var error = new Exception("Test exception");
            var statusCode = 500;

            // Act
            var appException = new AppException(code, message, error, statusCode, _mockLogger.Object);

            // Assert
            Assert.Contains(error.Message, appException.Message);
            Assert.DoesNotContain("ERROR_MESSAGE_NOT_AVAILABLE", appException.Message);
            Assert.StartsWith($"[ERROR]{code}::{message}", appException.Message);

            Assert.Equal(code, appException.Code);
            Assert.Equal(statusCode, appException.StatusCode);

        }

        [Fact]
        public void AppException_ModifiesMessage_WithoutException()
        {
            // Arrange
            var code = "TEST_CODE";
            var message = "Test message";
            var statusCode = 500;

            // Act
            var appException = new AppException(code, message, null, statusCode, _mockLogger.Object);

            // Assert
            Assert.DoesNotContain("InternalError:", appException.Message);
            Assert.Contains(message, appException.Message);
            Assert.StartsWith($"[ERROR]{code}::{message}", appException.Message);
        }


        [Fact]
        public void GetErrorResponse_ReturnsCorrectErrorResponse()
        {
            // Arrange
            var code = "TEST_CODE";
            var message = "Test message";
            var error = new Exception("Test exception");
            var statusCode = 500;
            var appException = new AppException(code, message, error, statusCode, _mockLogger.Object);
            var appExceptionWithoutError = new AppException(code, message, null, statusCode, _mockLogger.Object);

            var expectedResponse = new Dictionary<string, string>
            {
                { "code", code },
                { "message", message}, // mesagge is modified.
                { "innerError", error.Message },
                { "stackTrace", "STACK_TRACE_NOT_AVAILABLE" } // stack trace is not available in unit tests
            };

            Dictionary<string, string> expectedResponseWithoutError = new Dictionary<string, string>{
                { "code", code },
                { "message", message}, // mesagge is modified.
                { "innerError", "INNER_ERROR_NOT_AVAILABLE" },
                { "stackTrace", "STACK_TRACE_NOT_AVAILABLE" } // stack trace is not available in unit tests
            };

            // Act
            Dictionary<string, string> errorResponse = appException.GetErrorResponse();
            Dictionary<string, string> errorResponseWithoutError = appExceptionWithoutError.GetErrorResponse();

            // Assert
            Assert.IsType<Dictionary<string, string>>(errorResponse);
            Assert.Equivalent(expectedResponse, errorResponse);

            Assert.IsType<Dictionary<string, string>>(errorResponseWithoutError);
            Assert.Equivalent(expectedResponseWithoutError, errorResponseWithoutError);
        }

        /// <summary>
        /// Tests that the error is logged to the logger and verfies that the logged string contains the error code, message and the inner error message.
        /// </summary>
        [Fact]
        public void AppException_LogsError()
        {
            // Arrange
            var code = "TEST_CODE";
            var message = "Test message";
            var error = new Exception("Test exception");
            var statusCode = 500;

            // Act
            var appException = new AppException(code, message, error, statusCode, _mockLogger.Object);

            // Assert
            _mockLogger.Verify(
        x => x.Log(
            LogLevel.Error,
            It.IsAny<EventId>(),
            It.Is<It.IsAnyType>((v, t) => v.ToString().Contains(code) && v.ToString().Contains(message) && v.ToString().Contains(error.Message)),
            It.IsAny<Exception>(),
            (Func<It.IsAnyType, Exception, string>)It.IsAny<object>()),
        Times.Once);

        }


        [Fact]
        public void AppException_InternalError_ReturnsException()
        {
            // Arrange
            var code = "TEST_CODE";
            var message = "Test message";
            var error = new Exception("Test exception");
            var statusCode = 500;

            // Act
            var appException = new AppException(code, message, error, statusCode, _mockLogger.Object);

            // Assert
            Assert.Equal(error, appException.InternalError);
        }
    }


    /// <summary>
    /// Tests for ErrorCodes class. simple tests to check that the error codes are returned in the correct format.
    /// </summary>
    public class ErrorCodesTests
    {
        /// <summary>
        /// Tests that the error codes are string and in upper case.
        /// </summary>
        [Fact]
        public void ErrorCodes_ReturnsString_InUpperCase()
        {
            // Arrange
            // Act
            var invalidInput = ErrorCodes.InvalidInput;
            var unauthorizedAccess = ErrorCodes.UnauthorizedAccess;
            var databaseError = ErrorCodes.DatabaseError;
            var internalError = ErrorCodes.InternalError;

            // Assert
            Assert.IsType<string>(invalidInput);
            Assert.Equal(invalidInput, invalidInput.ToUpper());

            Assert.IsType<string>(unauthorizedAccess);
            Assert.Equal(unauthorizedAccess, unauthorizedAccess.ToUpper());

            Assert.IsType<string>(databaseError);
            Assert.Equal(databaseError, databaseError.ToUpper());

            Assert.IsType<string>(internalError);
            Assert.Equal(internalError, internalError.ToUpper());
        }

        /// <summary>
        /// Tests that the error codes does not contain spaces.
        /// </summary>
        [Fact]
        public void ErrorCodes_ReturnsString_WithoutSpaces()
        {
            // Arrange
            // Act
            var invalidInput = ErrorCodes.InvalidInput;
            var unauthorizedAccess = ErrorCodes.UnauthorizedAccess;
            var databaseError = ErrorCodes.DatabaseError;
            var internalError = ErrorCodes.InternalError;

            // Assert
            Assert.DoesNotContain(" ", invalidInput);
            Assert.DoesNotContain(" ", unauthorizedAccess);
            Assert.DoesNotContain(" ", databaseError);
            Assert.DoesNotContain(" ", internalError);
        }

    }


    public class AppModuleExceptionTests
    {
        [Fact]
        public void TestAppModuleExceptionConstructor()
        {
            // Arrange
            string module = "TestModule";
            string function = "TestFunction";
            string message = "TestMessage";
            Exception error = new Exception("TestException");
            // Act
            AppModuleException exception = new AppModuleException(module, function, message, error);

            // Assert
            Assert.Equal(ErrorCodes.InternalError, exception.Code);
            Assert.Equal($"[{module}][{function}]:{message}", exception.Message);
            Assert.Equal(error, exception.InnerException);
            Assert.Equal(500, exception.StatusCode);
        }
    }
}