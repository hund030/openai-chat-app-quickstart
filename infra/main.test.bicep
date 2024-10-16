// This file is for doing static analysis and contains sensible defaults
// for PSRule to minimise false-positives and provide the best results.

// This file is not intended to be used as a runtime configuration file.

targetScope = 'subscription'

param location string = 'eastus2'

module test 'main.bicep' = {
  name: 'test'
  params: {
    name: 'test'
    location: location
    createAzureOpenAi: true
    openAiDeploymentCapacity: 1
    openAiDeploymentName: 'test'
    openAiDeploymentSkuName: 'standard'
    openAiModelName: 'test'
    openAiModelVersion: '603'
    openAiResourceLocation: location
  }
}
