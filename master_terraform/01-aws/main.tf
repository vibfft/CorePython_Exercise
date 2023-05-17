terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region     = "us-east-1"
  access_key = "AKIASK7YQEYJ2RCTGXNW"
  secret_key = "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"
}

# create a vpc
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block

  tags = {
    "Name" = "${var.main_vpc_name}"
  }
}

# my vpc
# resource "aws_vpc" "myvpc" {
#   cidr_block = "192.168.0.0/16"

#   tags = {
#     "Name" = "My VPC"
#   }
# }

# create a subnet
resource "aws_subnet" "web" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.web_subnet
  availability_zone = "us-east-1a" # data center
  tags = {
    "Name" = "${var.web_subnet_name}"
  }
}

resource "aws_internet_gateway" "my_web_igw" {
  vpc_id = aws_vpc.main.id
  tags = {
    "Name" = "${var.main_vpc_name} IGW"
  }
}

resource "aws_default_route_table" "main_vpc_default_rt" {
  default_route_table_id = aws_vpc.main.default_route_table_id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my_web_igw.id
  }

  tags = {
    "Name" = "my-default-rt"
  }
}

resource "aws_default_security_group" "default_sec_group" {
  vpc_id = aws_vpc.main.id
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    # cidr_blocks = [var.var.my_public_ip]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    # cidr_blocks = [var.var.my_public_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    # cidr_blocks = [var.var.my_public_ip]
  }

  tags = {
    "Name" = "Default Security Group"
  }
}

# resource "aws_key_pair" "test_ssh_key" {
#     key_name = "testing_ssh_key"
#     public_key = file("$HOME/.ssh/test_rsa.pub")
# }

data "aws_ami" "latest_amazon_linux2" {
  owners      = ["amazon"]
  most_recent = true
  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-*-x86_64-gp2"]
  }
  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}

# resource "aws_instance" "my_vm" {
#     ami = "ami-06a0cd9728546d178"  # data.aws_ami.latest_amazon_linux2.id
#     instance_type = "t2.micro"
#     subnet_id = aws_subnet.web.id
#     vpc_security_group_ids = [aws_default_security_group.default_sec_group.id]
#     associate_public_ip_address = true
#     key_name = "production_ssh_key" # aws_key_pair.test_ssh_key.key_name
#     tags = {
#         "Name" = "My EC2 Instance - Amazon Linux 2"
#     }
# }