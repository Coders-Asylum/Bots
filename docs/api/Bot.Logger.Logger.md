# <a id="Bot_Logger_Logger"></a> Class Logger

Namespace: [Bot.Logger](Bot.Logger.md)  
Assembly: Bots.dll  

Logger to log messages to App Insights and to console.
This is added as a singleton service in Program.cs
and can be injected in any class.
<example> 
Usage:
<pre><code class="lang-csharp">public class SomeClass
{
private readonly Logger _logger;
public SomeClass(Logger logger)
{
_logger = logger;
}
public void SomeMethod()
{
_logger.Log.LogInformation("Some message");
}
}</code></pre>
</example>

```csharp
public class Logger
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Logger](Bot.Logger.Logger.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Constructors

### <a id="Bot_Logger_Logger__ctor_Microsoft_Extensions_Logging_ILoggerFactory_"></a> Logger\(ILoggerFactory\)

Logger to log messages to App Insights and to console.
This is added as a singleton service in Program.cs
and can be injected in any class.
<example> 
Usage:
<pre><code class="lang-csharp">public class SomeClass
{
private readonly Logger _logger;
public SomeClass(Logger logger)
{
_logger = logger;
}
public void SomeMethod()
{
_logger.Log.LogInformation("Some message");
}
}</code></pre>
</example>

```csharp
public Logger(ILoggerFactory loggerFactory)
```

#### Parameters

`loggerFactory` [ILoggerFactory](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.iloggerfactory)

Logger factory to create logger

## Properties

### <a id="Bot_Logger_Logger_Log"></a> Log

```csharp
public ILogger Log { get; }
```

#### Property Value

 [ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger)

