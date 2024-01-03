// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using Microsoft.Extensions.Logging;

namespace Bot.Logger
{
    /// <summary>
    ///    Logger to log messages to App Insights and to console.
    ///    This is added as a singleton service in <see cref="Program.cs"/>
    ///    and can be injected in any class.
    ///    <example> 
    ///    Usage:
    ///    <code>
    ///    public class SomeClass
    ///    {
    ///    private readonly Logger _logger;
    ///    public SomeClass(Logger logger)
    ///    {
    ///    _logger = logger;
    ///    }
    ///    public void SomeMethod()
    ///    {
    ///    _logger.Log.LogInformation("Some message");
    ///    }
    ///    }
    ///    </code>
    ///    </example>
    ///    </summary>
    ///    <param name="loggerFactory"> Logger factory to create logger </param>
    public class Logger(ILoggerFactory loggerFactory)
    {
        private readonly ILogger _logger = loggerFactory.CreateLogger("BOT");

        public ILogger Log
        {
            get
            {
                return _logger;
            }
        }
    }
}