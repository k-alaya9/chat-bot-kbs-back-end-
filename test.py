from flask import Flask, render_template
from experta import *
import os
from flask_socketio import SocketIO, send, emit
import socketio
import requests
import json
from threading import Event

#Hello World this is the final code KBS 




sio = socketio.Client()
stop_waiting_event = Event()


class Answer(Fact):
    cf = Field(float, default=1.0)

class question(Fact):
    pass


class DiagnosticExpert(KnowledgeEngine):

    @sio.event
    def recommend_action(self, action, cf=1):
        sio.emit("message",json.dumps({"answer":f"I recommend that you {action} (Certainty: {cf*100}%)\n","type":"q","chat_id":1}))
        print(f"I recommend that you {action} (Certainty: {cf*100}%)\n")

    @DefFacts()
    def init(self, **kwargs):
        self.current_question = None
        self.answer=None
        yield question(ident="unrecognized_email",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you have unrecognized emails?")
        
        yield question(ident="modified_data",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you have missing or modified data?")
        
        yield question(ident="browser_changes",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you have browser changes?")
        
        yield question(ident="random_messages",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you have random messages?")
        
        yield question(ident="ram_usage",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the RAM usage 75% or more?")
        
        yield question(ident="playing_games_ram",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are you playing games while RAM usage is high?")
        
        yield question(ident="many_programs",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you have many programs opened?")
        
        yield question(ident="app_crashes",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you suffer from applications crashing?")
        
        yield question(ident="strange_app",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there a strange application using RAM?")
        
        yield question(ident="cpu_usage",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the CPU usage 30% or more?")
        
        yield question(ident="playing_games_cpu",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are you playing games while CPU usage is high?")
        
        yield question(ident="slow_booting",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you suffer from slow booting?")
        
        yield question(ident="repeated_damages",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there any repeated damage?")
        
        yield question(ident="Cannot_connect",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Can't you connect to the network?")
        
        yield question(ident="disturbed_connection",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you suffer from disturbed connection?")
        
        yield question(ident="Verify_admin",
                       Type="multi",
                       valid=["user", "admin"],
                       text="Are you admin or user?")

        
        yield question(ident="confirm_server",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Can you confirm whether the server can ping the default gateway?")
        yield question(ident="resolving_domain names",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are you able to resolve domain names using DNS?")
        yield question(ident="interfacesUp_configured",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are all network interfaces up and configured correctly?")
        yield question(ident="confirm_routingTable",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Can you confirm that the server's routing table is correct?")
        yield question(ident="latency_packetLoss",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are you experiencing high latency or packet loss?")
        yield question(ident="blocking_traffic",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are there any firewall rules or security groups that might be blocking traffic?")
        yield question(ident="unusual_bandwidth",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there any unusual bandwidth usage on the network?")
        yield question(ident="static_dynamicIPadress",
                       Type="multi",
                       valid=["static", "dynamic"],
                       text="Is the server configured with a static or dynamic IP address?")
        yield question(ident="configured_correctly",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are the subnet mask and default gateway correctly configured ?")
        yield question(ident="conflict_IPaddress ",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there a possibility of an IP address conflict on the network?")
        yield question(ident="primary_secondary",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are the primary and secondary DNS servers reachable and configured correctly?")
        yield question(ident="clearing_cache",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Have you tried clearing the DNS cache on the server?")
        yield question(ident="congestion_bottlenecks",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are there any signs of network congestion or bottlenecks?")
        yield question(ident="Qos",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is Quality of Service(QoS) configured and does it prioritize critical traffic?")
        yield question(ident="VLANs",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are VALANs configured correctly on the server and network switches?")
        yield question(ident="MTU_settings",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are the MTU settings consistent across the network?")
        yield question(ident="NAT",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is NAT causing any issues with network traffic flow?")
        yield question(ident="intrusions",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there any instrusions in your network?")
        yield question(ident="unusual_patterns",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there unusual patterns such as unexpected large data transfers, conections to unknown IP addresses, or unusual port usage?")
        yield question(ident="suspicious_activities",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there any suspicious activities?")
        yield question(ident="unauthorized_access",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is there any sense of unauthorized access?")
        
#2
        yield question(ident="antivirus_software",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is antivirus software installed on the server?")
        yield question(ident="antivirus_uptodate",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the antivirus software up to date and actively scanning?")
        yield question(ident="malwares&files",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Has the antivirus detected any malware or suspicious files?")
        yield question(ident="high_severity_rating ",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is it a known malware with a high severty rating?")
        yield question(ident="removal_attempts",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the malware recurring despite removal attempts?")
        
        
        yield question(ident="have_firewall",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you have a firewall installed?")
        yield question(ident="configured_firewall",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the firewall configured correctly ?")
        yield question(ident="unuthorized_changes",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Have there been any unauthorized changes to the firewall configuration?")
        yield question(ident="Ip_turested",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the source IP address known and trusted?")
        yield question(ident="specific_port",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the traffic targeting a specific port or service repeatedly?")
        yield question(ident="traffic_pattern",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the traffic pattern consistent with normal activity?")
        yield question(ident="traffic_volume",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the traffic volume unusually high?")
        
        yield question(ident="unusual_activity",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Has there been any unusual activity involving user accounts?")
        
        yield question(ident="multiple_incorrect_logins",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Has there been an attempt to log in with multiple incorrect passwords?")
        
        yield question(ident="same_password_attempts",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Was the same password attempted across multiple accounts?")
        
        yield question(ident="all_users_authorized",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are all users on the system authorized?")
        
        yield question(ident="protected_files_accessed",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Have specific protected files been accessed or altered by unauthorized users?")
        #Last
        yield question(ident="server_ping", Type="multi", valid=["yes", "no"],
                       text="Can you confirm whether the server can ping the default gateway?")
        yield question(ident="connect_other_device", Type="multi", valid=["yes", "no"],
                       text="Can you connect to the network with another device?")
        yield question(ident="network_cable", Type="multi", valid=["yes", "no"],
                       text="Is the physical network cable connected?")
        yield question(ident="link_lights", Type="multi", valid=["yes", "no"],
                       text="Are the LED/Link lights on?")
        yield question(ident="network_adapter_enabled", Type="multi", valid=["yes", "no"],
                       text="Is the network adapter enabled?")
        yield question(ident="ip_config", Type="multi", valid=["dynamic", "static"],
                       text="Is the server configured with a static or dynamic IP address?")
        yield question(ident="dhcp_work", Type="multi", valid=["yes", "no"],
                       text="Check if the DHCP works.")
        yield question(ident="ip_conflict", Type="multi", valid=["yes", "no"],
                       text="Is there a possibility of an IP address conflict on the network?")
        yield question(ident="dhcp_pool", Type="multi", valid=["yes", "no"],
                       text="Check that the DHCP server's address pool still has addresses available.")
        
        yield question(ident="firewall_settings", Type="multi", valid=["yes", "no"], text="Are there any firewall settings blocking the connection?")
        yield question(ident="isp_settings", Type="multi", valid=["yes", "no"], text="Are the ISP settings correct?")
        yield question(ident="high_latency_packet_loss", Type="multi", valid=["yes", "no"], text="Are you experiencing high latency or packet loss?")
        yield question(ident="faulty_ethernet_port_cable", Type="multi", valid=["yes", "no"], text="Do you have a faulty ethernet port or cable?")
        yield question(ident="nic_issues", Type="multi", valid=["yes", "no"], text="Are there any issues with the network interface controller (NIC) in your PC?")
        yield question(ident="unusual_bandwidth_usage", Type="multi", valid=["yes", "no"], text="Is there any unusual bandwidth usage on the network?")
        yield question(ident="mtu_settings", Type="multi", valid=["yes", "no"], text="Are the MTU settings consistent across the network?")
        yield question(ident="nat_issues", Type="multi", valid=["yes", "no"], text="Is NAT causing any issues with network traffic flow?")
        yield question(ident="server_type", Type="multi", valid=["local server", "web server"], text="Are you trying to reach a local server or web server?")

        yield question(ident="unusual_traffic_patterns",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Have you identified any unusual traffic patterns or spikes at odd times?")
        yield question(ident="network_monitoring_tools",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are network monitoring tools (like Wireshark, NetFlow) being used to capture and analyze traffic?")
        yield question(ident="ids_deployed",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are Intrusion Detection Systems (IDS) like Snort or Suricata deployed and detecting known attack patterns?")
        yield question(ident="port_security",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Do you use port security to identify MAC addresses?")
        yield question(ident="unauthorized_devices",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are there any unknown or unauthorized devices on the network (use tools like Nmap)?")
        yield question(ident="suspicious_ip",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are there suspicious IP addresses involved in the traffic?")
        yield question(ident="Virus_Total",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Use services like VirusTotal to check if these IP addresses are associated with malicious activity! ")
        
        yield question(ident="Investigate",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Investigate the sources and destinations of this traffic.")
        
        yield question(ident="vlan_switch_config",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the VLAN configuration on the switch and server correct?")
        
        yield question(ident="server_nic_vlan",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the server’s NIC configured with the correct VLAN ID?")
        
        yield question(ident="switch_port_vlan",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are the switch port settings properly matched to the VLAN configuration requirements?")
        
        yield question(ident="trunk_ports_vlan",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are the trunk ports correctly configured to allow the necessary VLANs?")
        
        yield question(ident="trunking_protocols",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Have you checked that trunking protocols (e.g., 802.1Q) are properly set up on both the switch and server?")
        yield question(ident="switch_port_tagging",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is the switch port configured to handle VLAN tagging correctly?")
        
        yield question(ident="physical_connections",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are all the physical connections working?")

        yield question(ident="led_indicators",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are the LED indicators of your network cards lit?")

        yield question(ident="network_adapter_status",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Is your network adapter status working properly?")

        yield question(ident="network_settings",
                       Type="multi",
                       valid=["yes", "no"],
                       text="Are the network settings within the operating system correct?")
        
        yield question(ident="adequate_bandwidth", 
                       Type="multi", 
                       valid=["yes", "no"], 
                       text="Is the network designed with adequate bandwidth to handle peak traffic loads?")
        
        yield question(ident="sufficient_redundancy", 
                       Type="multi", 
                       valid=["yes", "no"], 
                       text="Does the network include sufficient redundancy?")
        
        yield question(ident="up_to_date_hardware", 
                       Type="multi", 
                       valid=["yes", "no"], 
                       text="Are all network hardware devices (routers, switches) up-to-date and capable of handling current throughput requirements?")
        
        yield question(ident="vlan_configuration", 
                       Type="multi", 
                       valid=["yes", "no"], 
                       text="Are VLANs configured correctly without causing broadcast storms or improper segmentation?")
        
        yield question(ident="qos_configuration", 
                       Type="multi", 
                       valid=["yes", "no"], 
                       text="Is Quality of Service (QoS) configured and does it prioritize critical traffic?")
        
        yield question(ident="hardware_works_fine", 
                       Type="multi", 
                       valid=["yes", "no"], 
                       text="Does all of the hardware devices work fine?")

        
    

    
        
        


    @Rule(NOT(Answer(ident='unrecognized_email')),
          NOT(Fact(ask='unrecognized_email')))
    def supply_answer_unrecognized_email(self):
        self.declare(Fact(ask='unrecognized_email'))

    # the rules when the user responds "no"
    @Rule(Answer(ident='unrecognized_email', text='no'))
    def no_unrecognized_email(self):
        self.declare(Fact(ask='modified_data'))

    @Rule(Answer(ident='modified_data', text='no'))
    def no_modified_data(self):
        self.declare(Fact(ask='browser_changes'))

    @Rule(Answer(ident='browser_changes', text='no'))
    def no_browser_changes(self):
        self.declare(Fact(ask='random_messages'))

    @Rule(Answer(ident='random_messages', text='no'))
    def no_attack_detected(self):
        print("Proceeding to RAM Flowchart.")
        self.declare(Fact(action='ram_diagnose'))

    #  when the user responds "yes"
    @Rule(Answer(ident='unrecognized_email', text='yes'))
    def yes_unrecognized_email(self):
        self.recommend_action("There is a  chance you are attacked, check with an expert.", 0.7)
        self.halt()
    
    @Rule(Answer(ident='modified_data', text='yes'))
    def yes_modified_data(self):
        self.recommend_action("There is a chance you are attacked, check with an expert.", 0.7)
        self.halt()
    
    @Rule(Answer(ident='browser_changes', text='yes'))
    def yes_browser_changes(self):
        self.recommend_action("There is a  chance you are attacked, check with an expert.", 0.7)
        self.halt()
    
    @Rule(Answer(ident='random_messages', text='yes'))
    def yes_random_messages(self):
        self.recommend_action("There is a  chance you are attacked, check with an expert.", 0.7)
        self.halt()

    # RAM Flowchart
    @Rule(Fact(action='ram_diagnose'), NOT(Answer(ident='ram_usage')), salience=6)
    def ask_ram_usage(self):
        self.current_question='ram_usage'
        response = self.ask_user("Is the RAM usage 75% or more? (yes/no): ", "multi", ["yes", "no"])
        print(response)
        self.declare(Answer(ident='ram_usage', text=response))

    @Rule(Answer(ident='ram_usage', text='yes'), NOT(Answer(ident='playing_games_ram')), salience=5)
    def check_playing_games(self):
        response = self.ask_user("Are you playing games? (yes/no): ", "multi", ["yes", "no"])
        # self.current_question
        print(response)
        if response == "yes":
            # print()
            self.recommend_action("Your RAM usage is high due to gaming. Consider upgrading your RAM orclosing unnecessary applications.", 0.8)
            #retry
            self.ask_ram_usage()
           
        else:
            self.declare(Answer(ident='playing_games_ram', text='no'))
    
    @Rule(Answer(ident='ram_usage', text='yes'), Answer(ident='playing_games_ram', text='no'), NOT(Answer(ident='many_programs')), salience=4)
    def check_many_programs(self):
        response = self.ask_user("Do you have a lot of programs opened? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            # print("Close unnecessary applications and retry.")
            self.recommend_action("Your RAM usage is high due to many programs opened. Close unnecessary applicationsand retry.", 0.8)
            #retry
            self.ask_ram_usage()
            
        else:
            self.declare(Answer(ident='many_programs', text='no'))

    @Rule(Answer(ident='ram_usage', text='yes'), Answer(ident='playing_games_ram', text='no'), Answer(ident='many_programs', text='no'), NOT(Answer(ident='app_crashes')), salience=3)
    def check_app_crashes(self):
        response = self.ask_user("Do you suffer from applications crashing? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            self.recommend_action("Consult an expert for RAM damage", 0.7)
            self.halt()
        else:
            self.declare(Answer(ident='app_crashes', text='no'))

    @Rule(Answer(ident='ram_usage', text='yes'), Answer(ident='playing_games_ram', text='no'), Answer(ident='many_programs', text='no'), Answer(ident='app_crashes', text='no'), NOT(Answer(ident='strange_app')), salience=2)
    def check_strange_app(self):
        response = self.ask_user("Is there a strange application using the RAM? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            self.recommend_action("You are attacked", 0.7)
            self.halt()
        else:
            self.declare(Answer(ident='strange_app', text='no'))

    @Rule(Answer(ident='ram_usage', text='yes'), Answer(ident='playing_games_ram', text='no'), Answer(ident='many_programs', text='no'), Answer(ident='app_crashes', text='no'), Answer(ident='strange_app', text='no'), salience=1)
    def check_ram(self):
        self.recommend_action("Check your RAM", 0.4)
        self.halt()

    @Rule(Answer(ident='ram_usage', text='no'), salience=0)
    def cpu_flowchart(self):
        print("Go to CPU Flowchart.")
        self.declare(Fact(action='cpu_diagnose'))

    # CPU Flowchart
    @Rule(Fact(action='cpu_diagnose'), NOT(Answer(ident='cpu_usage')), salience=6)
    def ask_cpu_usage(self):
        response = self.ask_user("Is the CPU usage 30% or more? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='cpu_usage', text=response))

    @Rule(Answer(ident='cpu_usage', text='yes'), NOT(Answer(ident='playing_games_cpu')), salience=5)
    def check_playing_games_cpu(self):
        response = self.ask_user("Are you playing games? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            # print("Close unnecessary applications and retry.")
            self.recommend_action("Close unnecessary applications and retry.", 0.8)
            self.ask_cpu_usage()
            self.halt()
        else:
            self.declare(Answer(ident='playing_games_cpu', text='no'))
    
    @Rule(Answer(ident='cpu_usage', text='yes'), Answer(ident='playing_games_cpu', text='no'), NOT(Answer(ident='slow_booting')), salience=4)
    def check_slow_booting(self):
        response = self.ask_user("Do you suffer from slow booting? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            self.recommend_action("Consult an expert for CPU damage", 0.7)
            self.halt()
        else:
            self.declare(Answer(ident='slow_booting', text='no'))

    @Rule(Answer(ident='cpu_usage', text='yes'), Answer(ident='playing_games_cpu', text='no'), Answer(ident='slow_booting', text='no'), NOT(Answer(ident='repeated_damages')), salience=3)
    def check_repeated_damages(self):
        response = self.ask_user("Is there any repeated damage? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            self.recommend_action("Consult an expert for CPU damage", 0.7)
            self.halt()
        else:
            self.recommend_action("Take precautions against potential attack", 0.4)
            self.halt()

    @Rule(Answer(ident='cpu_usage', text='no'), salience=2)
    def network_flowchart(self):
        print("Proceeding to Network Flowchart.")
       
        self.declare(Fact(action='network_diagnose'))

    # Network flowchart
    @Rule(Fact(action='network_diagnose'), NOT(Answer(ident='Cannot_connect')), salience=6)
    def ask_connect_network(self):
        response = self.ask_user("Can't you connect to the network? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='Cannot_connect', text=response))
        if response == "yes":
            # print("Check your network card.")
            self.recommend_action("Check your network card.", 0.8)
            self.halt()

    @Rule(Answer(ident='Cannot_connect', text='no'), NOT(Answer(ident='disturbed_connection')), salience=5)
    def check_disturbed_connection(self):
        response = self.ask_user("Do you suffer from disturbed connection? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            # print("Check your network card.")
            self.recommend_action("Check your network card.", 0.8)
            self.halt()
        else:
            self.declare(Answer(ident='disturbed_connection', text='no'))

    @Rule(Answer(ident='Cannot_connect', text='no'), Answer(ident='disturbed_connection', text='no'), NOT(Answer(ident='Verify_admin')), salience=4)
    def verify_admin(self):
        response = self.ask_user("Are you admin or user? (user/admin): ", "multi", ["user", "admin"])
        if response == "user":
            # print("please ask an expert.")
            self.recommend_action("Please ask an expert.", 0.9)
            self.halt()
        else:
            print("Proceeding to antivirus Flowchart.")
            self.declare(Fact(action='antivirus_diagnose'))
            #here farah

#antivirus_security flowchart
    @Rule(Fact(action='antivirus_diagnose'), NOT(Answer(ident='antivirus_software')), salience=8)
    def ask_antivirus_software(self):
        response = self.ask_user("Is antivirus software installed on the server? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='antivirus_software', text=response))
        if response == "no":
            # print("No antivirus software detected on the server.\n Seek expert assistance to install and configure antivirus protection immediately and to check for any attacks")
            self.recommend_action("No antivirus software detected on the server.\n Seek expert assistance to installand configure antivirus protection immediately and to check for any attacks", 0.9)
            self.halt()

    @Rule(Answer(ident='antivirus_software', text='yes'), NOT(Answer(ident='antivirus_uptodate')), salience=7)
    def check_antivirus_uptodate(self):
        response = self.ask_user("Is the antivirus software up to date and actively scanning? (yes/no): ", "multi", ["yes", "no"])
        if response == "no":
            self.recommend_action("Antivirus software is not up to date or no actively scanning .\n Seek expert assistance to installand configure antivirus protection immediately and to check for any attacks", 0.9)
            # print("Antivirus software is not up to date or no actively scanning .\n Seek expert asssistance to update and configure the antivirus software immedeatly and to check for any attacks.")
            self.halt()
        else:
            self.declare(Answer(ident='antivirus_uptodate', text='yes'))

    @Rule(Answer(ident='antivirus_software', text='yes'), Answer(ident='antivirus_uptodate', text='yes'), NOT(Answer(ident='malwares&files')), salience=6)
    def ask_servers_operation_uptodate(self):
        response = self.ask_user("Has the antivirus detected any malware or suspicious files? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            self.declare(Answer(ident='malwares&files', text='yes'))
    
        else:
            print("Proceeding to firewall Flowchart.")
            self.declare(Fact(action='firewall_diagnose'))
    @Rule(Answer(ident='antivirus_software', text='yes'), Answer(ident='antivirus_uptodate', text='yes'), Answer(ident='malwares&files', text='yes'),NOT(Answer(ident='high_severity_rating')), salience=5)
    def ask_antivirus_softwaree(self):
        response = self.ask_user("Is it a known malware with a high severty rating? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            
            self.recommend_action("Seek  expert assistance immedealtely.",0.85)
            self.halt()
        else:
            self.declare(Answer(ident='high_severity_rating', text='no'))
    @Rule(Answer(ident='antivirus_software', text='yes'), Answer(ident='antivirus_uptodate', text='yes'), Answer(ident='malwares&files', text='yes'), Answer(ident="high_severity_rating",text='no'),NOT(Answer(ident='removal_attempts')), salience=4)
    def ask_done(self):
        response = self.ask_user("Is the malware recurring despite removal attempts? (yes/no): ", "multi", ["yes", "no"])
        if response == "yes":
            self.recommend_action("Seek  expert assistance immedealtely.",0.80)
            self.halt()
        else:
            print("Proceeding to firewall Flowchart.")
            self.declare(Fact(action='firewall_diagnose'))
    
    #firewall flowchart
    @Rule(Fact(action='firewall_diagnose'), NOT(Answer(ident='have_firewall')), salience=9)
    def ask_firewall(self):
        response = self.ask_user("Do you have a firewall installed?: ", "multi", ["yes", "no"])
        self.declare(Answer(ident='have_firewall', text=response))
        if response == "no":
            # print("No firewall detected on the server.\n Seek expert assistance to install and configure firewall protection immedeatly and to check for any attacks.")
            self.recommend_action("No firewall detected on the server.\n Seek expert assistance to install andconfigure firewall protection immedeatly and to check for any attacks", 0.9)
            self.halt()

    @Rule(Answer(ident='have_firewall', text='yes'), NOT(Answer(ident='configured_firewall')), salience=8)
    def check_configured_firewall(self):
        response = self.ask_user("Is the firewall configured correctly ?: ", "multi", ["yes", "no"])
        if response == "no":
            # print("Firewall is not configured  correctly.\n Seek expert assistance to property configre the firewall immedeatly and to check for any attacks. ")
            self.recommend_action("Firewall is not configured  correctly.\n Seek expert assistance to property configure the firewall immedeatly and to check for any attacks. ", 0.8)
            self.halt()
        else:
            self.declare(Answer(ident='configured_firewall', text='yes'))

    @Rule(Answer(ident='have_firewall', text='yes'), Answer(ident='configured_firewall', text='yes'), NOT(Answer(ident='unuthorized_changes')), salience=7)
    def ask_unauthorized_changes(self):
        response = self.ask_user("Have there been any unauthorized changes to the firewall configuration? ", "multi", ["yes", "no"])
        if response == "no":
            print("Proceeding to user_privielge Flowchart.")
            self.declare(Fact(action='user_privielge_diagnose'))
        else:
            self.declare(Answer(ident='unuthorized_changes', text='yes'))
    @Rule(Answer(ident='have_firewall', text='yes'), Answer(ident='configured_firewall', text='yes'), Answer(ident='unuthorized_changes', text='yes'),NOT(Answer(ident='Ip_turested')), salience=6)
    def ask_antivirus_securityFlowchart(self):
        response = self.ask_user("Is the source IP address known and trusted? ", "multi", ["yes", "no"])
        if response == "no":
             self.declare(Answer(ident='Ip_turested', text='no'))
        else:
            self.declare(Answer(ident='Ip_turested', text='yes'))
    @Rule(Answer(ident='have_firewall', text='yes'), Answer(ident='configured_firewall', text='yes'), Answer(ident='unuthorized_changes', text='yes'),Answer(ident='Ip_turested',text='no'),NOT(Answer(ident='specific_port')), salience=5)
    def ask_specific_port(self):
        response = self.ask_user("Is the traffic targeting a specific port or service repeatedly? ", "multi", ["yes", "no"])
        if response == "no":
             self.declare(Answer(ident='specific_port', text='no'))
        else:
           self.recommend_action("Suspicious traffic detected .\n Seek expert assistance.",0.90)
           self.halt()
    @Rule(Answer(ident='have_firewall', text='yes'), Answer(ident='configured_firewall', text='yes'), Answer(ident='unuthorized_changes', text='yes'),Answer(ident='Ip_turested',text='no'),Answer(ident='specific_port',text='no'),NOT(Answer(ident='traffic_volume')), salience=4)
    def ask_traffic_volume(self):
        response = self.ask_user("Is the traffic volume unusually high? ", "multi", ["yes", "no"])
        if response == "no":
            print("Proceeding to user_privielge Flowchart.")
            self.declare(Fact(action='user_privielge_diagnose'))
        else:
            self.recommend_action("Potential DDoS attack detected .\n Seek expert assistance.",0.80)
            self.halt()
    @Rule(Answer(ident='have_firewall', text='yes'), Answer(ident='configured_firewall', text='yes'), Answer(ident='unuthorized_changes', text='yes'),Answer(ident='Ip_turested',text='yes'),NOT(Answer(ident='traffic_pattern')), salience=3)
    def ask_traffic_pattern(self):
        response = self.ask_user("Is the traffic pattern consistent with normal activity? ", "multi", ["yes", "no"])
        if response == "no":
            self.recommend_action("Unusual traffic pattern detected from a trusted source.\nSeek expert assistance.",0.75)
            self.halt()
        else:
           print("Proceeding to user_privilege Flowchart.")
           self.declare(Fact(action='user_privielge_diagnose'))

#...........user_privielge
    @Rule(Fact(action='user_privielge_diagnose'), NOT(Answer(ident='unusual_activity')), salience=6)
    def ask_unusual_activity(self):
        response = self.ask_user("Has there been any unusual activity involving user accounts? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='unusual_activity', text=response))

    @Rule(Answer(ident='unusual_activity', text='no'), NOT(Answer(ident='all_users_authorized')), salience=5)
    def ask_all_users_authorized(self):
        response = self.ask_user("Are all users on the system authorized?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='all_users_authorized', text=response))
        

    @Rule(Answer(ident='all_users_authorized', text='no'), salience=4)
    def unauthorized_users_detected(self):
        self.recommend_action("Unauthorized users detected. Seek expert assistance.", 0.9)
        self.halt()

    @Rule(Answer(ident='all_users_authorized', text='yes'), NOT(Answer(ident='protected_files_accessed')), salience=3)
    def ask_protected_files_accessed(self):
        response = self.ask_user("Have specific protected files been accessed or altered by unauthorized users? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='protected_files_accessed', text=response))

    @Rule(Answer(ident='protected_files_accessed', text='yes'), salience=2)
    def unauthorized_file_access(self):
        self.recommend_action("Unauthorized file access detected. Seek expert assistance.", 0.85)
        self.halt()

    @Rule(Answer(ident='protected_files_accessed', text='no'), salience=1)
    def no_specific_problem_detected(self):
        self.recommend_action("We couldn't detect a specific problem. But it's better to seek expert assistance.", 0.6)
        self.halt()

    @Rule(Answer(ident='unusual_activity', text='yes'), NOT(Answer(ident='multiple_incorrect_logins')), salience=5)
    def ask_multiple_incorrect_logins(self):
        response = self.ask_user("Has there been an attempt to log in with multiple incorrect passwords?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='multiple_incorrect_logins', text=response))

    @Rule(Answer(ident='multiple_incorrect_logins',text='no'),NOT(Answer(ident='all_users_authorized')), salience=4)
    def go_to_all_users_authorized(self):
        response = self.ask_user("Are all users on the system authorized? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='all_users_authorized', text=response))

    @Rule(Answer(ident='multiple_incorrect_logins', text='yes'), NOT(Answer(ident='same_password_attempts')), salience=3)
    def ask_same_password_attempts(self):
        response = self.ask_user("Was the same password attempted across multiple accounts? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='same_password_attempts', text=response))

    @Rule(Answer(ident='same_password_attempts', text='yes'), salience=2)
    def password_brute_force(self):
        self.recommend_action("Potential password brute force attack detected. Seek expert assistance.", 0.75)
        self.halt()

    @Rule(Answer(ident='same_password_attempts', text='no'), salience=1)
    def no_specific_problem_detected_after_incorrect_logins(self):
        print("continue to Connection problems")
        self.declare(Fact(action='connection_diagnose'))
    #...............Last
    #connection flowchart
    @Rule(Fact(action='connection_diagnose'), NOT(Answer(ident='server_ping')), salience=10)
    def ask_server_ping(self):
        response = self.ask_user("Can you confirm whether the server can ping the default gateway? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='server_ping', text=response))

    @Rule(Answer(ident='server_ping', text='no'), NOT(Answer(ident='ip_config')), salience=9)
    def ask_ip_config(self):
        response = self.ask_user("Is the server configured with a static or dynamic IP address?  ", "multi", ["dynamic", "static"])
        self.declare(Answer(ident='ip_config', text=response))
    @Rule(Answer(ident='ip_config', text='dynamic'), NOT(Answer(ident='dhcp_work')), salience=4)
    def ask_dhcp_work(self):
        response = self.ask_user("Check if the DHCP works ", "multi", ["yes", "no"])
        self.declare(Answer(ident='dhcp_work', text=response))
    @Rule(Answer(ident='dhcp_work',text='no'),NOT(Answer(ident='dhcp_pool')), salience=8)
    def ask_pool(self):
        response = self.ask_user("Check that the DHCP server's address pool still has addresses available", "multi", ["yes", "no"])
        if response == "no":
            self.recommend_action("Something is incorrect in the device comfiguration itself,not in the network or with the DHCP server.")
            self.halt()
        else:
            self.ask_connect_other_device()
    @Rule(Answer(ident='ip_config', text='static'), NOT(Answer(ident='ip_conflict')), salience=4)
    def resolve_ip_conflict(self):
        response = self.ask_user("Is there a possibility of an IP address conflict on the network? ", "multi", ["yes", "no"])
        if response == "no":
           self.ask_connect_other_device()
        else:
            self.recommend_action("Instruct on how to check for and resolve IP conflicts.")
            self.halt()
     
    @Rule(Answer(ident='dhcp_work',text='yes'),NOT(Answer(ident='connect_other_device')), salience=8)
    def ask_connect_other_device(self):
        response = self.ask_user("Can you connect to the network with another device? ", "multi", ["yes", "no"])
        if response == "no":
            self.recommend_action("Restart the network")
            self.halt()
        else:
            self.declare(Answer(ident='connect_other_device', text='yes'))
    @Rule(Answer(ident='connect_other_device',text='yes'),NOT(Answer(ident='network_cable')), salience=8)
    def ask_cnetwork_cable(self):
        response = self.ask_user("Is the physical network cable connected? ", "multi", ["yes", "no"])
        if response == "no":
            self.recommend_action("Reconect cable.")
            self.ask_server_ping()
            
        else:
            self.declare(Answer(ident='network_cable', text='yes'))

    @Rule(Answer(ident='network_cable', text='yes'), NOT(Answer(ident='link_lights')), salience=7)
    def ask_link_lights(self):
        response = self.ask_user("Are the LED/Link lights on?  ", "multi", ["yes", "no"])
        if response == "no":
            self.recommend_action("Change the cable.")
            self.ask_server_ping()
            
        else:
            self.declare(Answer(ident='link_lights', text='yes'))

    @Rule(Answer(ident='link_lights', text='yes'), NOT(Answer(ident='network_adapter_enabled')), salience=6)
    def ask_network_adapter_enabled(self):
        response = self.ask_user("Is the network adapter enabled? ", "multi", ["yes", "no"])
        if response == "no":
            self.recommend_action("Enable the network adapter")
            self.ask_server_ping()
        else:
            print("Proceeding to traffic Flowchart.")
            self.declare(Fact(action='traffic_diagnose'))

    @Rule(Answer(ident='server_ping', text='yes'), salience=0)
    def security_and_bandwidth_problems(self):
        print("Proceeding to traffic Flowchart.")
        self.declare(Fact(action='traffic_diagnose'))
#traffic flowchart

    @Rule(Fact(action='traffic_diagnose'), NOT(Answer(ident='firewall_settings')), salience=10)
    def ask_firewall_settings(self):
        response = self.ask_user("Are there any firewall settings blocking the connection? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='firewall_settings', text=response))

    @Rule(Answer(ident='firewall_settings', text='yes'), salience=9)
    def review_firewall_settings(self):
        self.recommend_action("Review and modify the firewall rules and settings.")
        self.halt()

    @Rule(Answer(ident='firewall_settings', text='no'), NOT(Answer(ident='isp_settings')), salience=8)
    def ask_isp_settings(self):
        response = self.ask_user("Are the ISP settings correct?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='isp_settings', text=response))

    @Rule(Answer(ident='isp_settings', text='no'), salience=7)
    def vlan_network_settings_problems(self):
        print("Continue to VLAN and network settings problems.")
        self.declare(Fact(action='VLAN_diagnose'))

    @Rule(Answer(ident='isp_settings', text='yes'), NOT(Answer(ident='high_latency_packet_loss')), salience=6)
    def ask_high_latency_packet_loss(self):
        response = self.ask_user("Are you experiencing high latency or packet loss?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='high_latency_packet_loss', text=response))
    @Rule(Answer(ident='high_latency_packet_loss', text='no'), NOT(Answer(ident='mtu_settings')), salience=5)
    def ask_mtu_settingss(self):
        response = self.ask_user("Are the MTU settings consistent across the network?  ", "multi", ["local server", "web server"])
        self.declare(Answer(ident='mtu_settings', text=response))
    @Rule(Answer(ident='high_latency_packet_loss', text='yes'), NOT(Answer(ident='faulty_ethernet_port_cable')), salience=4)
    def ask_faulty_ethernet_port_cable(self):
        response = self.ask_user("Do you have a faulty ethernet port or cable? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='faulty_ethernet_port_cable', text=response))

    @Rule(Answer(ident='faulty_ethernet_port_cable', text='yes'), salience=3)
    def change_cable_or_fix_port(self):
        self.recommend_action("Try to change the cable or fix the ethernet port.")
        self.halt()

    @Rule(Answer(ident='faulty_ethernet_port_cable', text='no'), NOT(Answer(ident='nic_issues')), salience=2)
    def ask_nic_issues(self):
        response = self.ask_user("Are there any issues with the network interface controller (NIC) in your PC? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='nic_issues', text=response))

    @Rule(Answer(ident='nic_issues', text='yes'), salience=1)
    def nic_problems(self):
       print("Flowchart to detect NIC problem.")
       self.declare(Fact(action='NIC_diagnose'))

    @Rule(Answer(ident='nic_issues', text='no'), NOT(Answer(ident='unusual_bandwidth_usage')), salience=0)
    def ask_unusual_bandwidth_usage(self):
        response = self.ask_user("Is there any unusual bandwidth usage on the network? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='unusual_bandwidth_usage', text=response))

    @Rule(Answer(ident='unusual_bandwidth_usage', text='yes'), salience=-1)
    def detect_hacking(self):
        print("Flowchart to detect hacking on unusual bandwidth usage on the network.")
        self.declare(Fact(action='hacking_diagnose'))

    @Rule(Answer(ident='unusual_bandwidth_usage', text='no'),  salience=-2)
    def continue_bad_design(self):
        print("Continue to bad_design problems.")
        self.declare(Fact(action='bad_design_diagnose'))

    @Rule(Answer(ident='mtu_settings', text='no'), salience=-3) 
    def verify_mtu_settings(self):
        self.recommend_action("Verify and standardize MTU settings to avoid fragmentation issues.")
        self.halt()
    @Rule(Answer(ident='mtu_settings', text='yes'), NOT(Answer(ident='server_type')), salience=-4)
    def ask_server_type_issues(self):
        response = self.ask_user("Are you trying to reach a local server or web server?", "multi", ["local server", "web server"])
        if response == "web server":
            self.declare(Answer(ident='server_type', text='web server'))
        else:
            print("Continue to VLAN and network settings problems.")
            self.declare(Fact(action='VLAN_diagnose'))
    @Rule(Answer(ident='server_type', text='web server'), NOT(Answer(ident='nat_issues')), salience=-4)
    def ask_nat_issues(self):
        response = self.ask_user("Is NAT causing any issues with network traffic flow? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='nat_issues', text=response))

    @Rule(Answer(ident='nat_issues', text='yes'), salience=-5)
    def adjust_nat_settings(self):
        self.recommend_action("Adjust NAT settings.")
        self.halt()

    @Rule(Answer(ident='nat_issues', text='no'), salience=-6)
    def call_expert(self):
        self.recommend_action("We couldn't determine the problem with the traffic, you should call an expert.")
        self.halt()
#hacking
    @Rule(Fact(action='hacking_diagnose'), NOT(Answer(ident='network_monitoring_tools')), salience=6)
    def ask_network_monitoring_tools(self):
        response = self.ask_user("Are network monitoring tools (like Wireshark, NetFlow) being used to capture and analyze traffic? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='network_monitoring_tools', text=response))
    @Rule(Answer(ident='network_monitoring_tools', text='no'), salience=2)
    def no_network_monitoring_tools(self):
        self.recommend_action("implement network\n monitoring tools to \n capture and analyze traffic \nfor unusual patterns.")

    @Rule(Answer(ident='network_monitoring_tools', text='yes'),NOT(Answer(ident='unusual_traffic_patterns')), salience=5)
    def yes_network_monitoring_tools(self):
        response=self.ask_user("Have you identified any unusual traffic patterns or spikes at odd times?","multi", ["yes", "no"])
        self.declare(Answer(ident='unusual_traffic_patterns', text=response))
    @Rule(Answer(ident='unusual_traffic_patterns', text='no',salience=4))
    def no_unusual_traffic_patterns(self):
        self.recommend_action("Continue to monitor traffic closely for any anomalies.")

    @Rule(Answer(ident='unusual_traffic_patterns', text='yes',salience=4),NOT(Answer(ident="Investigate")))
    def yes_unusual_traffic_patterns(self):
        response=self.ask_user('Investigate the sources and destinations of this traffic.',"multi", ["yes", "no"])
        self.declare(Answer(ident="Investigate",text=response))
    #implement CF
    @Rule(Answer(ident='Investigate', text='no',salience=4))
    def no_Investigate(self,cf1):
        cf_rule=0.8
        cf1=1.0
        self.recommend_action(' change the fire wall rules and if u still\n have this problem its\n a hacking attack you should call and \n security expert ',cf1*cf_rule)
        self.halt()
    @Rule(Answer(ident='Investigate', text='yes',salience=4),NOT(Answer(ident='unauthorized_devices')))
    def yes_Investigate(self,cf1):
        cf_rule=0.2
        cf1=1.0
        response=self.ask_user('Are there any unknown or unauthorized devices on the network (use tools like Nmap)?',"multi", ["yes", "no"])
        self.declare(Answer(ident="unauthorized_devices",text=response,cf=cf1*cf_rule))
   
    @Rule(Answer(ident='unauthorized_devices', text='yes'), salience=-1)
    def unauthorized_devices_detected(self):
        self.recommend_action("Identify and remove or quarantine these devices, got hacked!", 0.9)
        self.halt()
    
    @Rule(Answer(ident='unauthorized_devices', text='no'), NOT(Answer(ident='suspicious_ip')), salience=-2)
    def ask_suspicious_ip(self):
        response = self.ask_user("Are there suspicious IP addresses involved in the traffic? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='suspicious_ip', text=response))
    
    @Rule(Answer(ident='suspicious_ip', text='yes'),  NOT(Answer(ident='port_security')),salience=-3)
    def ask_port_security(self):
        response = self.ask_user("Do you use port security to identify MAC addresses? ","multi", ["yes", "no"] )
        self.declare(Answer(ident='port_security', text=response))
    
    @Rule(Answer(ident='suspicious_ip', text='no'),NOT(Answer(ident='ids_deployed')), salience=-4)
    def no_suspicious_ip(self):
       response = self.ask_user(" Are Intrusion Detection Systems (IDS) like Snort or Suricata deployed and detecting known attack patterns? ","multi", ["yes", "no"])
       self.declare(Answer(ident='ids_deployed', text=response))

    @Rule(Answer(ident='port_security', text='no'), salience=-6)
    def no_port_security(self):
        self.recommend_action("Enable port security, it's probably one of your users trying to connect with an unknown device.", 0.6)
        self.halt()
    
    @Rule(Answer(ident='port_security', text='yes'), NOT(Answer(ident='Virus_Total')),salience=-7)
    def port_security_enabled(self):
        response = self.ask_user(" Use services like VirusTotal to check if these IP addresses are associated with malicious activity!  ","multi", ["yes", "no"])
        self.declare(Answer(ident='Virus_Total', text=response))
    @Rule(Answer(ident='Virus_Total', text='yes'))
    def yes_Virus_Total(self):
        self.recommend_action(" Block the IP and  rescan your Server to see if there any malicious programs  , got hacked", 0.9)
        self.halt()
    @Rule(Answer(ident='Virus_Total', text='no'), NOT(Answer(ident='ids_deployed')),salience=-7)
    def no_Virus_Total(self):
        self.no_suspicious_ip()
    @Rule(Answer(ident='ids_deployed', text='yes'))
    def yes_Virus_Total(self):
        self.recommend_action("  Investigate any alerts generated by the IDS.")
        self.halt()
    @Rule(Answer(ident='ids_deployed', text='no'))
    def yes_Virus_Total(self):
        self.recommend_action("Deploy IPS and configure them to detect known attack patterns and prevernt them.")
        self.halt()

#VLAN FLOWCHART
    @Rule(Fact(action='VLAN_diagnose'), NOT(Answer(ident='vlan_switch_config')), salience=6)
    def ask_vlan_switch_config(self):
        response = self.ask_user("Is the VLAN configuration on the switch and server correct? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='vlan_switch_config', text=response))

    @Rule(Answer(ident='vlan_switch_config', text='no'), salience=5)
    def fix_vlan_switch_config(self):
        self.recommend_action("Configure the correct setting for VLAN on the switch and server", 0.9)
        self.halt()

    @Rule(Answer(ident='vlan_switch_config', text='yes'), NOT(Answer(ident='server_nic_vlan')), salience=5)
    def ask_server_nic_vlan(self):
        response = self.ask_user("Is the server’s NIC configured with the correct VLAN ID?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='server_nic_vlan', text=response))

    @Rule(Answer(ident='server_nic_vlan', text='no'), salience=4)
    def fix_server_nic_vlan(self):
        self.recommend_action("Ensure the server’s NIC is configured with the correct VLAN ID", 0.9)
        self.halt()

    @Rule(Answer(ident='vlan_switch_config', text='yes'), Answer(ident='server_nic_vlan', text='yes'), NOT(Answer(ident='switch_port_vlan')), salience=4)
    def ask_switch_port_vlan(self):
        response = self.ask_user("Are the switch port settings properly matched to the VLAN configuration requirements? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='switch_port_vlan', text=response))

    @Rule(Answer(ident='switch_port_vlan', text='no'), salience=3)
    def fix_switch_port_vlan(self):
        self.recommend_action("Set the switch port settings to match the VLAN configuration", 0.9)
        self.halt()

    @Rule(Answer(ident='vlan_switch_config', text='yes'), Answer(ident='server_nic_vlan', text='yes'), Answer(ident='switch_port_vlan', text='yes'), NOT(Answer(ident='trunk_ports_vlan')), salience=3)
    def ask_trunk_ports_vlan(self):
        response = self.ask_user("Are the trunk ports correctly configured to allow the necessary VLANs? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='trunk_ports_vlan', text=response))

    @Rule(Answer(ident='trunk_ports_vlan', text='no'), salience=2)
    def fix_trunk_ports_vlan(self):
        self.recommend_action("Correct the trunk ports to allow the necessary VLANs", 0.9)
        self.halt()

    @Rule(Answer(ident='vlan_switch_config', text='yes'), Answer(ident='server_nic_vlan', text='yes'), Answer(ident='switch_port_vlan', text='yes'), Answer(ident='trunk_ports_vlan', text='yes'), NOT(Answer(ident='trunking_protocols')), salience=2)
    def ask_trunking_protocols(self):
        response = self.ask_user("Have you checked that trunking protocols (e.g., 802.1Q) are properly set up on both the switch and server? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='trunking_protocols', text=response))

    @Rule(Answer(ident='trunking_protocols', text='no'), salience=1)
    def fix_trunking_protocols(self):
        self.recommend_action("Set up trunking protocols (e.g., 802.1Q) properly on both the switch and server", 0.9)
        self.halt()

    @Rule(Answer(ident='vlan_switch_config', text='yes'), Answer(ident='server_nic_vlan', text='yes'), Answer(ident='switch_port_vlan', text='yes'), Answer(ident='trunk_ports_vlan', text='yes'), Answer(ident='trunking_protocols', text='yes'), NOT(Answer(ident='switch_port_tagging')), salience=1)
    def ask_switch_port_tagging(self):
        response = self.ask_user("Is the switch port configured to handle VLAN tagging correctly? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='switch_port_tagging', text=response))

    @Rule(Answer(ident='switch_port_tagging', text='no'), salience=0)
    def fix_switch_port_tagging(self):
        self.recommend_action("Ensure the switch port is configured to handle VLAN tagging correctly", 0.9)
        self.halt()

    @Rule(Answer(ident='vlan_switch_config', text='yes'), Answer(ident='server_nic_vlan', text='yes'), Answer(ident='switch_port_vlan', text='yes'), Answer(ident='trunk_ports_vlan', text='yes'), Answer(ident='trunking_protocols', text='yes'), Answer(ident='switch_port_tagging', text='yes'), salience=0)
    def call_expert(self):
        self.recommend_action("Call an expert", 1.0)
        self.halt()
#NIC FLOWCHART
    @Rule(Fact(action='NIC_diagnose'), NOT(Answer(ident='physical_connections')), salience=5)
    def ask_physical_connections(self):
        response = self.ask_user("Are all the physical connections working? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='physical_connections', text=response))

    @Rule(Answer(ident='physical_connections', text='no'))
    def check_physical_connections(self):
        self.recommend_action("Make sure all the network cables or optical cables and network cards are firmly and properly seated in ports or slots without loose or unplugged.\nYou can try to unplug the cards and insert them again.")
        self.halt()

    @Rule(Answer(ident='physical_connections', text='yes'), NOT(Answer(ident='led_indicators')), salience=4)
    def ask_led_indicators(self):
        response = self.ask_user("Are the LED indicators of your network cards lit?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='led_indicators', text=response))

    @Rule(Answer(ident='led_indicators', text='no'))
    def check_led_indicators(self):
        self.recommend_action("Insert cables or adapters in different ports or slots to see whether the ports or slots are damaged. If the problem persists, change to new cables or NIC cards.")
        self.halt()

    @Rule(Answer(ident='led_indicators', text='yes'), NOT(Answer(ident='network_adapter_status')), salience=3)
    def ask_network_adapter_status(self):
        response = self.ask_user("Is your network adapter status working properly? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='network_adapter_status', text=response))

    @Rule(Answer(ident='network_adapter_status', text='no'))
    def check_network_adapter_status(self):
        self.recommend_action("There might be some specific problems with your card.")
        self.halt()

    @Rule(Answer(ident='network_adapter_status', text='yes'), NOT(Answer(ident='network_settings')), salience=2)
    def ask_network_settings(self):
        response = self.ask_user("Are the network settings within the operating system correct?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='network_settings', text=response))

    @Rule(Answer(ident='network_settings', text='no'))
    def correct_network_settings(self):
        self.recommend_action("Correct the network settings within your operating system.")
        self.halt()

    @Rule(Answer(ident='network_settings', text='yes'), salience=1)
    def diagnose_completed(self):
        self.recommend_action("If all checks are correct, the network should be working properly. If not, You need to change the network interface card probably or call an expert to help you.")
        self.halt()
    #bad design
    @Rule(Fact(action='bad_design_diagnose'), NOT(Answer(ident='qos_configuration')), salience=6)
    
    def ask_qos_configuration(self):
        response = self.ask_user("Is Quality of Service (QoS) configured and does it prioritize critical traffic? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='qos_configuration', text=response))
    @Rule(Answer(ident='qos_configuration', text='no'), salience=5)
    def qos_issue(self):
        self.recommend_action("Incorrect setting on routers,switches,and\n other network devices can\n cause inefficies and packet drops, \n you need an expert to\nconfigure it.")
        self.halt()
    @Rule(Answer(ident='qos_configuration', text='yes'),NOT(Answer(ident='adequate_bandwidth')) ,salience=5)
    def ask_adequate_bandwidth(self):
        response = self.ask_user("Is the network designed with adequate bandwidth to handle peak traffic loads? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='adequate_bandwidth', text=response))

    @Rule(Answer(ident='adequate_bandwidth', text='no'), salience=5)
    def insufficient_bandwidth(self):
        self.recommend_action("Review network design to ensure it can handle peak loads due to insufficient bandwidth causing congestion.", 0.8)
        self.halt()

    @Rule(Answer(ident='adequate_bandwidth', text='yes'), NOT(Answer(ident='sufficient_redundancy')), salience=5)
    def ask_sufficient_redundancy(self):
        response = self.ask_user("Does the network include sufficient redundancy? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='sufficient_redundancy', text=response))

    @Rule(Answer(ident='sufficient_redundancy', text='no'), salience=4)
    def insufficient_redundancy(self):
        self.recommend_action("A lack of redundancy means there are no\n alternate paths for data\n during failures or congestion,\n leadingto packetloss.\n Enhacing network redundancy is \n necassery.", 0.7)
        self.halt()

    @Rule(Answer(ident='sufficient_redundancy', text='yes'), NOT(Answer(ident='up_to_date_hardware')), salience=4)
    def ask_up_to_date_hardware(self):
        response = self.ask_user("Are all network hardware devices (routers, switches) up-to-date and capable of handling current throughput requirements?  ", "multi", ["yes", "no"])
        self.declare(Answer(ident='up_to_date_hardware', text=response))

    @Rule(Answer(ident='up_to_date_hardware', text='no'), salience=3)
    def outdated_hardware(self):
        self.recommend_action("Upgrade hardware to meet current requirements is recommended as faulty or outdated hardware can lead to packet loss.", 0.7)
        self.halt()

    @Rule(Answer(ident='up_to_date_hardware', text='yes'), NOT(Answer(ident='vlan_configuration')), salience=3)
    def ask_vlan_configuration(self):
        response = self.ask_user("Are VLANs configured correctly without causing broadcast storms or improper segmentation? ", "multi", ["yes", "no"])
        self.declare(Answer(ident='vlan_configuration', text=response))

    @Rule(Answer(ident='vlan_configuration', text='no'), salience=2)
    def vlan_issue(self):
        print("Continue to VLAN and network settings problems as incorrect VLAN configurations can cause issues.")
        self.declare(Fact(action='VLAN_diagnose'))

    @Rule(Answer(ident='vlan_configuration', text='yes'), NOT(Answer(ident='qos_configuration')), salience=2)
    def ask_hardware_works_fine(self):
        response = self.ask_user("Does all of the hardware devices work fine? (yes/no): ", "multi", ["yes", "no"])
        self.declare(Answer(ident='hardware_works_fine', text=response))

    @Rule(Answer(ident='hardware_works_fine', text='no'), salience=0)
    def hardware_issue(self):
        self.recommend_action("Fix or change the faulty hardware devices.", 0.7)
        self.halt()

    @Rule(Answer(ident='hardware_works_fine', text='yes'), salience=0)
    def network_design_not_cause(self):
        self.recommend_action("The network design is less likely to be the cause of packet loss.", 0.4)
        self.halt()

    @sio.event
    def ask_user(self, question, Type, valid=None,):
        answer = ""
        stop_waiting_event.clear()
        valid_answers = "Valid answers are: " + " / ".join(valid)
        sio.emit('message', json.dumps({"answer": question, "type": "q", "chat_id": 1, "valid": valid_answers}))
        stop_waiting_event.wait()
        print(self.answer)
        answer=self.answer

        # while not self.is_of_type(answer, Type, valid):
        #     print(question,flush=True)
        #     if Type == "multi":
        #         print("Valid answers are: ", " / ".join(valid))
        #     answer = input().strip().lower()
        return answer

    def is_a_number(self, answer):
        try:
            int(answer)
            return True
        except ValueError:
            return False

    def is_of_type(self, answer, Type, valid):
        if Type == "multi":
            return answer in valid
        if Type == "number":
            return self.is_a_number(answer)
        return len(answer) > 0

    @Rule(question(ident=MATCH.id, text=MATCH.text, valid=MATCH.valid, Type=MATCH.Type),
          NOT(Answer(ident=MATCH.id)),
          AS.ask << Fact(ask=MATCH.id))
    @sio.event
    def ask_question_by_id(self, ask, id, text, valid, Type):
        self.retract(ask)
        self.current_question=id
        self.ask_user(text,Type,valid)
        self.declare(Answer(ident=id, text=self.answer))
        # sio.wait(0)

    
    def calculate_CF(self,cf_data,cf_rule,cf_conclusion):
        cf_conclusion=cf_data*cf_rule

    def combine_cf(self, cf1, cf2):
        if cf1 >= 0 and cf2 >= 0:
            return cf1 + cf2 - cf1 * cf2
        elif cf1 < 0 and cf2 < 0:
            return cf1 + cf2 + cf1 * cf2
        else:
            return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))
       
  
expert=DiagnosticExpert()
@sio.event
def message(data):
    print(data)
    if data != "user connected!":
        answer = data.get('answer')
        typeM=data.get('type')
        chat_id = data.get('chat_id')
        print("Received message: ", answer)
        print(expert.current_question)
        # Process the received message and declare it as an Answer fact
        if typeM!='q':
            expert.answer=answer
            stop_waiting_event.set()
@sio.event
def connect():
    expert.reset()
    expert.run()
    print('Connection established')

if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.wait()
