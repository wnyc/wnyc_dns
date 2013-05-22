import boto

def load(domains):
    cxn = boto.connect_route53()
    for domain in domains:
        response = route53.create_hosted_zone(domain.name)
        
