# Get folder by id
data "google_folder" "my_folder_1" {
  folder              = "folders/12345"
  lookup_organization = true
}