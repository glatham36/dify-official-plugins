# S3 Compatible Storage Privacy Policy

This plugin connects to S3-compatible storage services (such as MinIO, Amazon S3, DigitalOcean Spaces, etc.) to access and retrieve files. 

## Data Processing

- The plugin only accesses files that you explicitly request through the datasource interface
- No file content is stored or cached by the plugin
- All authentication credentials are handled securely and are not logged or transmitted to third parties
- File metadata (names, sizes, types) may be temporarily processed during file browsing operations

## Credentials Security

- Access keys and secret keys are stored securely within the Dify platform
- Credentials are only used to authenticate with your specified S3-compatible storage endpoint
- No credentials are shared with external services other than your configured storage provider

## Network Communication

- All communication with your S3-compatible storage service uses the endpoint URL you provide
- SSL/TLS encryption is supported and configurable
- No data is transmitted to services other than your configured storage provider

## Data Retention

- No persistent data storage occurs within this plugin
- File content is streamed directly from your storage service to the Dify platform
- No copies of your files are retained after processing

For questions about this privacy policy, please contact the plugin maintainers.