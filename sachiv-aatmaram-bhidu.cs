using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace Sachiv.Function
{
    public class sachiv_aatmaram_bhidu
    {
        private readonly ILogger _logger;

        public sachiv_aatmaram_bhidu(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<sachiv_aatmaram_bhidu>();
        }

        [Function("sachiv_aatmaram_bhidu")]
        public HttpResponseData Run([HttpTrigger(AuthorizationLevel.Anonymous, "get", "post")] HttpRequestData req)
        {
            _logger.LogInformation("C# HTTP trigger function processed a request.");

            var response = req.CreateResponse(HttpStatusCode.OK);
            response.Headers.Add("Content-Type", "text/plain; charset=utf-8");

            response.WriteString("Welcome to Azure Functions!");

            return response;
        }
    }
}
