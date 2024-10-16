// This file is for doing static analysis and contains sensible defaults
// for PSRule to minimise false-positives and provide the best results.
// This file is not intended to be used as a runtime configuration file.

targetScope = 'subscription'

module test 'main.bicep' = {
  name: 'test'
  params: {
    name: 'test'
    location: 'test'
    principalId: 'test'
    createRoleForUser: true
    acaExists: true
    openAiResourceName: 'test'
    openAiResourceGroupName: 'test'
    openAiResourceLocation: 'eastus'
    openAiSkuName: 'test'
    openAiApiVersion: 'test'
    disableKeyBasedAuth: true
    openAiDeploymentName: 'test'
    openAiModelName: 'test'
    openAiModelVersion: 'test'
    openAiDeploymentCapacity: 1
    openAiDeploymentSkuName: 'test'
    createAzureOpenAi: true
    openAiEndpoint: 'test'
  }
}
