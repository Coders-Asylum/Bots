using System.Text.Json;

namespace Bot.Src.Config
{
    public class Configuration
    {
        public Dictionary<string, dynamic> localConfig = [];
        private static readonly bool hasBeenLoaded = false;
        static Configuration()
        {
            // run load config once for all instances.
            if (!hasBeenLoaded)
            {
                Configuration config = new();
                config.LoadConfig();
                hasBeenLoaded = true;
            }
        }

        /// <summary>
        /// Loads config from the local config file.
        /// 
        /// The config file is expected to be in JSON format and path must be set in the `CONFIG_PATH` env variable.
        /// </summary>
        /// <exception cref="Exception">If config env variable is not found or value is null.</exception>
        /// <exception cref="Exception">If the config file contents is null.</exception>
        public void LoadConfig()
        {
            //read from env variable
            string configPath = Environment.GetEnvironmentVariable("CONFIG_PATH") ?? throw new Exception("CONFIG_PATH env variable not found");
            string configFileContents = File.ReadAllText(configPath);
            localConfig = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(configFileContents) ?? throw new Exception("Config file found is empty");
        }

    }
}