variable "vpc_cidr_block" {
  default     = "10.0.0.0/16"
  description = "CIDR Block for VPC"
  type        = string
}

variable "web_subnet" {
  default     = "10.0.10.0/24"
  description = "Web Subnet"
  type        = string
}

variable "main_vpc_name" {
  type = string
}

variable "web_subnet_name" {
  type = string
}

variable "my_public_ip" {

}