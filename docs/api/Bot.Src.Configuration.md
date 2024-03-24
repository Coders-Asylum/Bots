# <a id="Bot_Src_Configuration"></a> Class Configuration

Namespace: [Bot.Src](Bot.Src.md)  
Assembly: Bots.dll  

```csharp
public class Configuration
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Configuration](Bot.Src.Configuration.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Constructors

### <a id="Bot_Src_Configuration__ctor_System_String_"></a> Configuration\(string\)

```csharp
public Configuration(string appId)
```

#### Parameters

`appId` [string](https://learn.microsoft.com/dotnet/api/system.string)

## Properties

### <a id="Bot_Src_Configuration_AppId"></a> AppId

Application id of the bot.

```csharp
public static string AppId { get; }
```

#### Property Value

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Bot_Src_Configuration_HasBeenLoaded"></a> HasBeenLoaded

Flag to check if the config has been loaded.

```csharp
public static bool HasBeenLoaded { get; }
```

#### Property Value

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Bot_Src_Configuration_LocalConfig"></a> LocalConfig

Returns the local config.

```csharp
public static Dictionary<string, dynamic> LocalConfig { get; }
```

#### Property Value

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), dynamic\>

## Methods

### <a id="Bot_Src_Configuration_LoadConfig"></a> LoadConfig\(\)

Loads config from the local config file.

The config file is expected to be in JSON format and path must be set in the `CONFIG_PATH` env variable.
This method is called automatically when the Configuration class is initialised, no need of callig it explicitly.

```csharp
public static void LoadConfig()
```

#### Exceptions

 [Exception](https://learn.microsoft.com/dotnet/api/system.exception)

If config env variable is not found or value is null.

 [Exception](https://learn.microsoft.com/dotnet/api/system.exception)

If the config file contents is null.

