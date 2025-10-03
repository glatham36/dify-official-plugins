# S3 Compatible Storage Datasource Plugin

This plugin provides a datasource for S3-compatible storage services, including MinIO, Amazon S3, DigitalOcean Spaces, and other S3-compatible object storage providers.

## Features

- Browse buckets and files in S3-compatible storage
- Download files for processing in Dify workflows
- Support for custom endpoint URLs (essential for MinIO and other self-hosted solutions)
- Configurable SSL/TLS settings
- Path-style addressing for maximum compatibility

## Configuration

The plugin requires the following configuration parameters:

### Required Parameters

- **Endpoint URL**: The URL of your S3-compatible storage service
  - For MinIO: `http://localhost:9000` (or your MinIO server URL)
  - For DigitalOcean Spaces: `https://nyc3.digitaloceanspaces.com` (region-specific)
  - For Amazon S3: `https://s3.amazonaws.com` or region-specific endpoint
  
- **Access Key ID**: Your storage service access key ID
- **Secret Access Key**: Your storage service secret access key

### Optional Parameters

- **Region Name**: Storage region (defaults to `us-east-1` if not specified)
- **Use SSL**: Whether to use SSL/TLS encryption (defaults to `false`)

## Supported Storage Services

This plugin has been designed to work with any S3-compatible storage service, including:

- **MinIO**: Open source object storage server
- **Amazon S3**: AWS Simple Storage Service
- **DigitalOcean Spaces**: DigitalOcean's object storage
- **Backblaze B2**: With S3-compatible API
- **Wasabi**: Cloud storage service
- **IBM Cloud Object Storage**: With S3-compatible API
- **Google Cloud Storage**: With S3-compatible API (interoperability mode)

## Usage Examples

### MinIO Configuration
```
Endpoint URL: http://localhost:9000
Access Key ID: your-minio-access-key
Secret Access Key: your-minio-secret-key
Region Name: us-east-1 (or leave empty)
Use SSL: false (for local MinIO without TLS)
```

### DigitalOcean Spaces Configuration
```
Endpoint URL: https://nyc3.digitaloceanspaces.com
Access Key ID: your-spaces-access-key
Secret Access Key: your-spaces-secret-key
Region Name: nyc3
Use SSL: true
```

## Security Considerations

- Always use SSL/TLS (`Use SSL: true`) for production environments
- Keep your access keys secure and rotate them regularly
- Use least-privilege access keys that only have permissions for the buckets you need
- For MinIO and other self-hosted solutions, ensure proper network security

## Troubleshooting

### Connection Issues
- Verify the endpoint URL is correct and accessible
- Check if SSL/TLS settings match your server configuration
- Ensure network connectivity to the storage service

### Authentication Issues
- Verify access key ID and secret access key are correct
- Check that the keys have proper permissions for the operations you're trying to perform
- For MinIO, ensure the user has the necessary policies attached

### Bucket Access Issues
- Verify the bucket exists and you have access to it
- Check bucket policies and access control lists
- Ensure the region setting matches where your bucket is located

## Development

This plugin is built using the Dify plugin framework and uses the boto3 library for S3 API compatibility.

### Dependencies
- dify_plugin==0.5.0b14
- boto3

## License

This plugin follows the same license as the Dify project.