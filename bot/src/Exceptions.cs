// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using System.Drawing.Text;
using Bots.Src.Utils;
using Microsoft.Extensions.Logging;

namespace Bot.Exceptions
{

    /// <summary>
    ///    Custom error codes to be used in <see cref="AppException"/>
    ///    Use these codes to construct custom error messages.
    /// </summary>
    public static class ErrorCodes
    {
        /// <value>
        /// Error code for invalid input
        /// </value>
        public static readonly string InvalidInput = "INVALID_INPUT";
        /// <value>
        /// Error code for unauthorized access
        /// </value>
        public static readonly string UnauthorizedAccess = "UNAUTHORIZED_ACCESS";
        /// <value>
        /// Error code for database errors
        /// </value>
        public static readonly string DatabaseError = "DATABASE_ERROR";
        /// <value>
        /// Error code for internal errors
        /// </value>
        public static readonly string InternalError = "INTERNAL_ERROR";
    }

    /// <summary>
    ///     Constructs custom error message to add more information to the original error.
    ///     Also generates the error response to be sent to the client.
    ///     Logs the error to App Insights. and to console.
    /// </summary>
    public class AppException : Exception
    {

        private readonly Exception? _error;

        private readonly Dictionary<string, string> _errorResponse;

        /// <param name="code"> A custom error codes, use one of <see cref="ErrorCodes"/>, or Error code in the format of `CUSTOM_ERROR_CODE` </param>
        /// <param name="message"> Error custom message to make it easier for clients to understnad</param>
        /// <param name="error">The actual captured internal error,if any</param>
        /// <param name="statusCode">An HTTP status code for this error, will be returned as response. Defaults to 500</param>
        /// <param name="logger"> A logger instance to be passed</param>
        public AppException(string code, string message, Exception? error, int statusCode, ILogger logger) : base($"[ERROR]{code}::{message}" + (error != null ? $"\n-InternalError: {error.Message}" : ""), error)
        {
            Code = code;
            StatusCode = statusCode;
            _error = error;
            _errorResponse = new Dictionary<string, string>
            {
                {"code", code },
                {"message", message },
                {"innerError", error?.Message ?? "INNER_ERROR_NOT_AVAILABLE"},
                {"stackTrace", error?.StackTrace ?? "STACK_TRACE_NOT_AVAILABLE"}
            };
            logger.LogError("[ERROR]{code}::{message}- InternalError: {error.Message}", code, message, _error?.Message ?? "ERROR_MESSAGE_NOT_AVAILABLE");
        }


        /// <value> custom Error code for this error, will be returned as response.</value>
        public string Code { get; }

        /// <value> HTTP status code for this error, will be returned as response.</value>
        public int StatusCode { get; }

        /// <summary> The actual captured internal error,if any</summary>
        public Exception? InternalError => _error;


        ///<summary>
        //Error response to be sent to the client.
        ///</summary>
        public Dictionary<string, string> GetErrorResponse()
        {
            return _errorResponse;
        }

    }


    /// <summary>
    ///   Exceptions caught with the module and function details.
    ///   Use this class to throw exceptions from within module and function details.
    /// <example>
    ///    <code>
    ///    throw new ModuleException("MODULE_NAME", "FUNCTION_NAME", "ERROR_MESSAGE", exception);
    ///    </code>
    ///  </example>
    ///</summary>
    /// <remarks>
    ///  <para>
    ///  This class is used to throw exceptions from within module and function details.
    ///  </para>
    ///  <para>
    /// <remarks>
    ///   Constructs a new instance of the <see cref="AppModuleException"/> class.
    /// </remarks>
    /// <param name="module">The module name.</param>
    /// <param name="function">The function name.</param>
    /// <param name="message">The error message.</param>
    /// <param name="error">The actual captured internal error,if any</param>
    /// </summary>
    public class AppModuleException(string module, string function, string message, Exception? error) : AppException(ErrorCodes.InternalError, $"[{module}][{function}]:{message}", error, HTTPStatus.INTERNAL_SERVER_ERROR, new Logger<AppModuleException>(new LoggerFactory()))
    {
    }

}