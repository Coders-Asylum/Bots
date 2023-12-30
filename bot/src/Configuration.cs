using System.Text.Json;

namespace Bot.Src
{
    public static class Configuration
    {
        private static Dictionary<string, dynamic> _localConfig = new();
        /// <summary>
        /// A flag to check if the config has been loaded.
        /// </summary>
        private static readonly bool _hasBeenLoaded;
        static Configuration()
        {
            if (!_hasBeenLoaded)
            {
                // Any thing that must be loaded once, must be called before this line.
                _hasBeenLoaded = true;
            }


        }

        /// <summary>
        /// Loads config from the local config file.
        /// 
        /// The config file is expected to be in JSON format and path must be set in the `CONFIG_PATH` env variable.
        /// This method is called automatically when the Configuration class is initialised, no need of callig it explicitly.
        /// </summary>
        /// <exception cref="Exception">If config env variable is not found or value is null.</exception>
        /// <exception cref="Exception">If the config file contents is null.</exception>
        public static void LoadConfig()
        {
            //read from env variable
            string configPath = Environment.GetEnvironmentVariable("CONFIG_PATH") ?? throw new Exception("CONFIG_PATH env variable not found");
            string configFileContents = File.ReadAllText(configPath);
            if (configFileContents == "" || configFileContents == null)
            {
                // todo: @Maverick099 to look if error really needs to be thrown here.
                throw new Exception("Config file found is empty.");
            }
            try
            {
                _localConfig = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(configFileContents) ?? [];

            }
            catch (Exception e)
            {
                // wrap the exception in a more meaningful with actual exception message
                throw new Exception($"Config file is not valid json file.Error:{e.Message}");
            }
        }

        /// <summary>
        /// Returns the local config.
        /// </summary>
        /// <returns>A </returns>
        public static Dictionary<string, dynamic> LocalConfig
        {
            get
            {
                if (_localConfig == null || _localConfig.Count == 0)
                {
                    LoadConfig();
                }

                return _localConfig ?? [];
            }
        }

        /// <summary>
        /// Flag to check if the config has been loaded.
        /// </summary>
        /// <returns>True if the config has already been loaded.</returns>
        public static bool HasBeenLoaded
        {
            get
            {
                return _hasBeenLoaded;
            }
        }
    }
}