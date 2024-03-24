# <a id="Bot_Exceptions_AppModuleException"></a> Class AppModuleException

Namespace: [Bot.Exceptions](Bot.Exceptions.md)  
Assembly: Bots.dll  

```csharp
public class AppModuleException : AppException, ISerializable
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) ← 
[AppException](Bot.Exceptions.AppException.md) ← 
[AppModuleException](Bot.Exceptions.AppModuleException.md)

#### Implements

[ISerializable](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.iserializable)

#### Inherited Members

[AppException.Code](Bot.Exceptions.AppException.md\#Bot\_Exceptions\_AppException\_Code), 
[AppException.StatusCode](Bot.Exceptions.AppException.md\#Bot\_Exceptions\_AppException\_StatusCode), 
[AppException.InternalError](Bot.Exceptions.AppException.md\#Bot\_Exceptions\_AppException\_InternalError), 
[AppException.GetErrorResponse\(\)](Bot.Exceptions.AppException.md\#Bot\_Exceptions\_AppException\_GetErrorResponse), 
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

### <a id="Bot_Exceptions_AppModuleException__ctor_System_String_System_String_System_String_System_Exception_"></a> AppModuleException\(string, string, string, Exception?\)

```csharp
public AppModuleException(string module, string function, string message, Exception? error)
```

#### Parameters

`module` [string](https://learn.microsoft.com/dotnet/api/system.string)

`function` [string](https://learn.microsoft.com/dotnet/api/system.string)

`message` [string](https://learn.microsoft.com/dotnet/api/system.string)

`error` [Exception](https://learn.microsoft.com/dotnet/api/system.exception)?

