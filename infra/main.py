#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance, InstanceEbsBlockDevice
from cdktf_cdktf_provider_aws.security_group import SecurityGroup, SecurityGroupIngress, SecurityGroupEgress
from user_data import user_data_node_manager, user_data_http1, user_data_bdd1

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region="us-east-1")

        security_group = SecurityGroup(
            self, "sg-tp",
            ingress=[
                SecurityGroupIngress(
                    from_port=22,
                    to_port=22,
                    cidr_blocks=["0.0.0.0/0"],
                    protocol="TCP",
                    description="Accept incoming SSH connection"
                    ),
                SecurityGroupIngress(
                    from_port=80,
                    to_port=80,
                    cidr_blocks=["0.0.0.0/0"],
                    protocol="TCP",
                    description="Accept incoming HTTP connection"
                    )
                ],
            egress=[
                SecurityGroupEgress(
                    from_port=0,
                    to_port=0,
                    cidr_blocks=["0.0.0.0/0"],
                    protocol="-1",
                    description="allow all egresse connection"
                    )
            ]
        )

        instance_manager = Instance(self,
                           "node-manager",
                           ami="ami-0557a15b87f6559cf",
                           tags={"Name": "node-manager"},
                           instance_type="t2.micro",
                           security_groups=[security_group.name],
                           key_name="vockey",
                           user_data_base64= user_data_node_manager, 
                           ebs_block_device= [
                               InstanceEbsBlockDevice(
                                   device_name="/dev/sda1",
                                   delete_on_termination=True,
                                   encrypted=False,
                                   volume_size=20,
                                   volume_type="gp2"
                               ),
                               InstanceEbsBlockDevice(
                                   device_name="/dev/sdb",
                                   delete_on_termination=True,
                                   encrypted=False,
                                   volume_size=100,
                                   volume_type="gp2"
                               ) 
                           ]
                                                      
                           )


        instance_http1 = Instance(self,
                           "node-http1",
                           ami="ami-0557a15b87f6559cf",
                           tags={"Name": "node-http1"},
                           instance_type="t2.micro",
                           security_groups=[security_group.name],
                           key_name="vockey",
                           user_data_base64= user_data_http1, 
                           ebs_block_device= [
                               InstanceEbsBlockDevice(
                                   device_name="/dev/sda1",
                                   delete_on_termination=True,
                                   encrypted=False,
                                   volume_size=20,
                                   volume_type="gp2"
                               ),
                               InstanceEbsBlockDevice(
                                   device_name="/dev/sdb",
                                   delete_on_termination=True,
                                   encrypted=False,
                                   volume_size=100,
                                   volume_type="gp2"
                               ) 
                           ]
                                                      
                           )


        instance_bdd1 = Instance(self,
                           "node-bdd1",
                           ami="ami-0557a15b87f6559cf",
                           tags={"Name": "node-bdd1"},
                           instance_type="t2.micro",
                           security_groups=[security_group.name],
                           key_name="vockey",
                           user_data_base64= user_data_bdd1, 
                           ebs_block_device= [
                               InstanceEbsBlockDevice(
                                   device_name="/dev/sda1",
                                   delete_on_termination=True,
                                   encrypted=False,
                                   volume_size=20,
                                   volume_type="gp2"
                               ),
                               InstanceEbsBlockDevice(
                                   device_name="/dev/sdb",
                                   delete_on_termination=True,
                                   encrypted=False,
                                   volume_size=100,
                                   volume_type="gp2"
                               ) 
                           ]
                                                      
                           )



        TerraformOutput(
            self, "public_node_manager_ip",
            value=instance_manager.public_ip,
            )


        TerraformOutput(
            self, "public_node_http1_ip",
            value=instance_http1.public_ip,
            )


        TerraformOutput(
            self, "public_node_bdd1_ip",
            value=instance_bdd1.public_ip,
            )


app = App()
MyStack(app, "ansible1")

app.synth()
