# <a id="Bots_FunctionExecutorHostBuilderExtensions"></a> Class FunctionExecutorHostBuilderExtensions

Namespace: [Bots](Bots.md)  
Assembly: Bots.dll  

Extension methods to enable registration of the custom <xref href="Microsoft.Azure.Functions.Worker.Invocation.IFunctionExecutor" data-throw-if-not-resolved="false"></xref> implementation generated for the current worker.

```csharp
public static class FunctionExecutorHostBuilderExtensions
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[FunctionExecutorHostBuilderExtensions](Bots.FunctionExecutorHostBuilderExtensions.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Methods

### <a id="Bots_FunctionExecutorHostBuilderExtensions_ConfigureGeneratedFunctionExecutor_Microsoft_Extensions_Hosting_IHostBuilder_"></a> ConfigureGeneratedFunctionExecutor\(IHostBuilder\)

Configures an optimized function executor to the invocation pipeline.

```csharp
public static IHostBuilder ConfigureGeneratedFunctionExecutor(this IHostBuilder builder)
```

#### Parameters

`builder` [IHostBuilder](https://learn.microsoft.com/dotnet/api/microsoft.extensions.hosting.ihostbuilder)

#### Returns

 [IHostBuilder](https://learn.microsoft.com/dotnet/api/microsoft.extensions.hosting.ihostbuilder)

