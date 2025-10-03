from typing import Any, Mapping

from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from dify_plugin.interfaces.datasource import DatasourceProvider
import boto3  # type: ignore
from botocore.client import Config  # type: ignore


class S3CompatibleStorageDatasourceProvider(DatasourceProvider):
    def _validate_credentials(self, credentials: Mapping[str, Any]) -> None:
        try:
            if not credentials or not credentials.get("secret_access_key"):
                raise ToolProviderCredentialValidationError(
                    "Secret access key is required."
                )
            if not credentials.get("access_key_id"):
                raise ToolProviderCredentialValidationError(
                    "Access key ID is required."
                )
            if not credentials.get("endpoint_url"):
                raise ToolProviderCredentialValidationError(
                    "Endpoint URL is required."
                )
            
            # Set default region if not provided
            region_name = credentials.get("region_name") or "us-east-1"
            
            # Configure SSL based on user preference
            use_ssl = credentials.get("use_ssl", False)
            
            client = boto3.client(
                "s3",
                aws_secret_access_key=credentials.get("secret_access_key"),
                aws_access_key_id=credentials.get("access_key_id"),
                endpoint_url=credentials.get("endpoint_url"),
                region_name=region_name,
                use_ssl=use_ssl,
                config=Config(s3={"addressing_style": "path"}),
            )
            client.list_buckets()
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))