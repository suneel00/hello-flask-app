output "jenkins_instance_ip" {
  value = aws_instance.jenkins_host.public_ip
}
