def convertit_ip(ip):
    ip_liste = ip.split('.')
    for i in range(4):
        ip_liste[i] = int(ip_liste[i])
    return ip_liste

def et_logique(ip1, ip2):



class Pc:
    def __init__(self, configuration_reseau):
        self.nom = configuration_reseau['nom']
        self.ip = configuration_reseau['ip']
        self.masque = configuration_reseau['masque']
        self.passerelle = configuration_reseau['passerelle']
        self.voisins = []
    def raccorder(self, v):
        self.voisins.append(v)
        if self not in v.voisins:
            v.raccorder(self)
    def est_dans_meme_reseau(self, v):
        if v not in self.voisins:
            return False



class Routeur:
    def __init__(self, configuration_reseau):
        self.nom = configuration_reseau['nom']
        self.ip = configuration_reseau['ip']
        self.masque = configuration_reseau['masque']
        self.voisins = []
    def raccorder(self, v):
        self.voisins.append(v)
        if self not in v.voisins:
            v.raccorder(self)

PC01 = Pc({'nom': 'PC01',
            'ip': '192.168.1.1',
            'masque': '255.255.255.0',
            'passerelle': '192.168.1.254'})
PC02 = Pc({'nom': 'PC02',
            'ip': '192.168.1.2',
            'masque': '255.255.255.0',
            'passerelle': '192.168.1.254'})

R01 = Routeur({'nom': 'R01',
                'ip': '192.168.1.254',
                'masque': '255.255.255.0'})

PC01.raccorder(R01)

