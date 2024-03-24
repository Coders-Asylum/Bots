# <a id="Bot_Exceptions_AppException"></a> Class AppException

Namespace: [Bot.Exceptions](Bot.Exceptions.md)  
Assembly: Bots.dll  

Constructs custom error message to add more information to the original error.
Also generates the error response to be sent to the client.
Logs the error to App Insights. and to console.

```csharp
public class AppException : Exception, ISerializable
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) ← 
[AppException](Bot.Exceptions.AppException.md)

#### Derived

[AppModuleException](Bot.Exceptions.AppModuleException.md)

#### Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)

#### Inherited Members

[Exception.GetBaseException\(\)](https://learn.microsoft.com/dotnet/api/system.exception.getbaseexception), 
[Exception.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.exception.gettype), 
[Exception.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.exception.tostring), 
[Exception.Data](https://learn.microsoft.com/dotnet/api/system.exception.data), 
[Exception.HelpLink](https://learn.microsoft.com/dotnet/api/system.exception.helplink), 
[Exception.HResult](https://learn.microsoft.com/dotnet/api/system.exception.hresult), 
[Exception.InnerException](https://learn.microsoft.com/dotnet/api/system.exception.innerexception), 
[Exception.Message](https://learn.microsoft.com/dotnet/api/system.exception.message), 
[Exception.Source](https://learn.microsoft.com/dotnet/api/system.exception.source), 
[Exception.StackTrace](https://learn.microsoft.com/dotnet/api/system.exception.stacktrace), 
[Exception.TargetSite](https://learn.microsoft.com/dotnet/api/system.exception.targetsite), 
[Exception.SerializeObjectState](https://learn.microsoft.com/dotnet/api/system.exception.serializeobjectstate), 
[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Constructors

### <a id="Bot_Exceptions_AppException__ctor_System_String_System_String_System_Exception_System_Int32_Microsoft_Extensions_Logging_ILogger_"></a> AppException\(string, string, Exception?, int, ILogger\)

```csharp
public AppException(string code, string message, Exception? error, int statusCode, ILogger logger)
```

#### Parameters

`code` [string](https://learn.microsoft.com/dotnet/api/system.string)

A custom error codes, use one of <xref href="Bot.Exceptions.ErrorCodes" data-throw-if-not-resolved="false"></xref>, or Error code in the format of `CUSTOM_ERROR_CODE`

`message` [string](https://learn.microsoft.com/dotnet/api/system.string)

Error custom message to make it easier for clients to understnad

`error` [Exception](https://learn.microsoft.com/dotnet/api/system.exception)?

The actual captured internal error,if any

`statusCode` [int](https://learn.microsoft.com/dotnet/api/system.int32)

An HTTP status code for this error, will be returned as response. Defaults to 500

`logger` [ILogger](https://learn.microsoft.com/dotnet/api/microsoft.extensions.logging.ilogger)

A logger instance to be passed

## Properties

### <a id="Bot_Exceptions_AppException_Code"></a> Code

```csharp
public string Code { get; }
```

#### Property Value

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Bot_Exceptions_AppException_InternalError"></a> InternalError

The actual captured internal error,if any

```csharp
public Exception? InternalError { get; }
```

#### Property Value

 [Exception](https://learn.microsoft.com/dotnet/api/system.exception)?

### <a id="Bot_Exceptions_AppException_StatusCode"></a> StatusCode

```csharp
public int StatusCode { get; }
```

#### Property Value

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## Methods

### <a id="Bot_Exceptions_AppException_GetErrorResponse"></a> GetErrorResponse\(\)

```csharp
public Dictionary<string, string> GetErrorResponse()
```

#### Returns

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

