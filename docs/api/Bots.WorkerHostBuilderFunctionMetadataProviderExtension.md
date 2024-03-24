# <a id="Bots_WorkerHostBuilderFunctionMetadataProviderExtension"></a> Class WorkerHostBuilderFunctionMetadataProviderExtension

Namespace: [Bots](Bots.md)  
Assembly: Bots.dll  

Extension methods to enable registration of the custom <xref href="Microsoft.Azure.Functions.Worker.Core.FunctionMetadata.IFunctionMetadataProvider" data-throw-if-not-resolved="false"></xref> implementation generated for the current worker.

```csharp
public static class WorkerHostBuilderFunctionMetadataProviderExtension
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[WorkerHostBuilderFunctionMetadataProviderExtension](Bots.WorkerHostBuilderFunctionMetadataProviderExtension.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Methods

### <a id="Bots_WorkerHostBuilderFunctionMetadataProviderExtension_ConfigureGeneratedFunctionMetadataProvider_Microsoft_Extensions_Hosting_IHostBuilder_"></a> ConfigureGeneratedFunctionMetadataProvider\(IHostBuilder\)

Adds the GeneratedFunctionMetadataProvider to the service collection.
During initialization, the worker will return generated function metadata instead of relying on the Azure Functions host for function indexing.

```csharp
public static IHostBuilder ConfigureGeneratedFunctionMetadataProvider(this IHostBuilder builder)
```

#### Parameters

`builder` [IHostBuilder](https://learn.microsoft.com/dotnet/api/microsoft.extensions.hosting.ihostbuilder)

#### Returns

 [IHostBuilder](https://learn.microsoft.com/dotnet/api/microsoft.extensions.hosting.ihostbuilder)

