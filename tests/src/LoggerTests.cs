// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using Xunit;
using Microsoft.Extensions.Logging;
using Moq;
using Bot.Logger;

namespace Tests.Src
{
    /// <summary>
    ///    Tests for <see cref="Logger"/>
    ///    This not an comprehensive test,just enough to make sure the logger is being created and returned correctly.
    ///    Will not be adding more tests unless there is a change in the logger class, related to its format and on a custom functioanlity added to it.
    /// </summary>

    public class LoggerTests
    {
        private readonly Mock<ILoggerFactory> _mockLoggerFactory;
        private readonly Mock<ILogger> _mockLogger;

        public LoggerTests()
        {
            _mockLoggerFactory = new Mock<ILoggerFactory>();
            _mockLogger = new Mock<ILogger>();

            _mockLoggerFactory.Setup(x => x.CreateLogger(It.IsAny<string>())).Returns(_mockLogger.Object);
        }

        [Fact]
        public void Logger_CreatesLogger_OnConstruction()
        {
            // Arrange
            // Act
            var logger = new Logger(_mockLoggerFactory.Object);

            // Assert
            _mockLoggerFactory.Verify(x => x.CreateLogger("BOT"), Times.Once);
        }

        [Fact]
        public void Logger_ReturnsLogger_OnGetLog()
        {
            // Arrange
            var logger = new Logger(_mockLoggerFactory.Object);

            // Act
            var result = logger.Log;

            // Assert
            Assert.Equal(_mockLogger.Object, result);
        }
    }
}