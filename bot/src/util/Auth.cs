// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Timers;
using Microsoft.IdentityModel.Tokens;
//

namespace Bot.Src.Utils
{
    /// <summary>
    /// Authentication related utilities.
    /// </summary>
    public class Authentication
    {
        static Authentication()
        {

        }
        /// <summary>
        /// Generates the singned JWT token, Using the private pem key string, so algoritm is RSA256.
        /// </summary>
        public static string GenerateSignedJWTToken(IEnumerable<Claim> claims, string privateKey)
        {
            RSA decodedPEMKey = DecodePrivatePEMKey(privateKey);
            RsaSecurityKey securityKey = new(decodedPEMKey);
            SigningCredentials credentials = new(securityKey, SecurityAlgorithms.RsaSha256);
            JwtSecurityToken token = new(claims: claims, signingCredentials: credentials);
            // the generated bearer token
            return new JwtSecurityTokenHandler().WriteToken(token);
        }

        /// <summary>
        /// Checks if the given token is expired or not
        /// </summary>
        public static bool IsTokenExpired(string token)
        {
            JwtSecurityTokenHandler tokenHandler = new();
            JwtSecurityToken jwtToken = tokenHandler.ReadJwtToken(token);
            return jwtToken.ValidTo < DateTime.UtcNow;
        }

        /// <summary>
        /// Decodes the private key from the PEM format.
        /// </summary>
        /// <param name="privateKey">The PEM file/string contents.</param>
        /// <returns>RSA object</returns>
        public static RSA DecodePrivatePEMKey(string privateKey)
        {
            RSA rsa = RSA.Create();
            rsa.ImportFromPem(privateKey);
            return rsa;
        }

        public static string GithubAppJWTToken(string appid, string privateKey)
        {
            DateTime now = DateTime.UtcNow;
            // delete a minitue from the current time to allow clock drift.
            long unixTime = new DateTimeOffset(now.AddMinutes(-1)).ToUnixTimeSeconds();
            IEnumerable<Claim> claims =
            [
                new(JwtRegisteredClaimNames.Iat, unixTime.ToString()),
                new (JwtRegisteredClaimNames.Exp, (unixTime + (60 * 10)).ToString()), // 10 minutes
                new(JwtRegisteredClaimNames.Iss, appid)
            ];
            return GenerateSignedJWTToken(claims, privateKey);
        }

    }
}