// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

namespace Bots.Src.Utils
{
    /// <summary>
    /// Constants used in the Appication throughout.
    /// </summary>
    public readonly struct Constants
    {
        /// <value>
        /// Environment variable name for config path.
        /// </value>
        public const string CONFIG_PATH_ENV = "CONFIG_PATH";
    }


    /// <summary>
    /// Different types of Security Algorithms.
    /// </summary>
    public readonly struct Algorithms
    {
        /// <value>
        /// HMAC using SHA-256 hash algorithm.
        /// </value>
        public const string RS256 = "RS256";
        /// <value>
        /// HMAC using SHA-384 hash algorithm.
        /// </value>
        public const string RS384 = "RS384";



    }

    /// <summary>
    /// Different HTTP Statuses
    /// </summary>
    public readonly struct HTTPStatus
    {
        /// <value>
        /// HTTP Status Code 200
        /// </value>
        public const int OK = 200;
        /// <value>
        /// HTTP Status Code 201
        /// </value>
        public const int CREATED = 201;
        /// <value>
        /// HTTP Status Code 400
        /// </value>
        public const int BAD_REQUEST = 400;
        /// <value>
        /// HTTP Status Code 401
        /// </value>
        public const int UNAUTHORIZED = 401;
        /// <value>
        /// HTTP Status Code 403
        /// </value>
        public const int FORBIDDEN = 403;
        /// <value>
        /// HTTP Status Code 404
        /// </value>
        public const int NOT_FOUND = 404;
        /// <value>
        /// HTTP Status Code 500
        /// </value>
        public const int INTERNAL_SERVER_ERROR = 500;
        /// <value>
        /// HTTP Status Code 503
        /// </value>
        public const int SERVICE_UNAVAILABLE = 503;
        /// <value>
        /// HTTP Status Code 504
        /// </value>
        public const int GATEWAY_TIMEOUT = 504;
    }
}