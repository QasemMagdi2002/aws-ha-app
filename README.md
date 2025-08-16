# AWS HA App (ALB • ASG • RDS • SQS • Lambda • WAF)

Production-style reference architecture built for learning + portfolio:
- VPC (public/private, 2 AZ) with IGW + NAT
- HTTPS via ACM/Route53 → ALB → EC2 Auto Scaling (Dockerized FastAPI)
- RDS PostgreSQL (private subnets)
- SQS decoupling with Lambda consumer → DynamoDB
- WAF (AWS Managed Core + rate limiting)
- CloudWatch alarms + SNS

## Code
- `app/` — FastAPI web API (Docker)
- `lambda/` — SQS → DynamoDB consumer (Python)
- `docs/` — architecture diagram, console runbook, test checklist

## Quick local test
```bash
docker build -t aws-ha-app:local app
docker run -p 8080:8080 aws-ha-app:local
# http://localhost:8080/health
