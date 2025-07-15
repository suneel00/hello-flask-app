variable "aws_region" {
  default = "us-east-1"
}

variable "ami_id" {
  description = "Ubuntu AMI ID"
  type        = string
}

variable "key_name" {
  description = "Your AWS EC2 key pair name"
  type        = string
}
