terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.30.0"
    }
  }
}

provider "google" {
  # Configuration options
    
    project = "custom-autumn-449504-f9"
    region  = "us-central1"
    zone    = "us-central1-a"
}