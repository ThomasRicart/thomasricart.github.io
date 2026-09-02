class IPv4(object):
    def __init__(self, adresse:str):
        """ Constructeur de la classe de calcul sur une adresse IPv4
        dont la notation décimale pointée est passée en paramètre. """
        self.adresse = adresse
    def octets(self):
        """ Découpe l'adresse décimale pointée en la liste des 4 entiers
        correspondants. """
        return [int(i) for i in self.adresse.split(".")]
    def masquer(self, masque: str)->str:
        """ Détermine le préfixe masqué de l'adresse,
        le masque (décimal pointé) étant passé en paramètre.
        >>> ip01 = IPv4('192.168.1.100')
        >>> ip01.masquer('255.192.0.0')
        '192.128.0.0'        """
        tmp = []
        ip = self.octets()
        crible = IPv4(masque).octets()
        for i in range(4):
            tmp.append(ip[i] & crible[i])               # Question 08
        return ".".join([str(k) for k in tmp])          # Question 08

    def adresse_suivante(self, adresse_max:str)->str:
        """ Détermine l'adresse décimale pointée suivant immédiatement
        l'adresse courante, sous réserve d'existence d'une adresse disponible
        >>> ip01 = IPv4('192.168.1.100')
        >>> ip01.adresse_suivante('192.168.1.254')
        '192.168.1.101'
        >>> ip01 = IPv4('192.168.1.255')
        >>> ip01.adresse_suivante('192.168.255.254')
        '192.168.2.0'        """
        assert self.adresse < adresse_max
        liste_courante = self.octets()
        liste_suivante = list()
        retenue = 1
        for index in range(4):
            somme = liste_courante[3 - index] + retenue
            valeur, retenue = somme%256, somme//256             # Question 08
            liste_suivante = [str(valeur)] + liste_suivante     # Question 08
        return '.'.join(liste_suivante)

ip01 = IPv4('192.168.1.100')
ip02 = IPv4('192.168.1.255')
ip03 = IPv4('192.168.2.5')

assert ip01.octets() == [192, 168, 1, 100]
assert ip01.masquer('255.192.0.0') == '192.128.0.0'
assert ip01.adresse_suivante('192.168.1.254') == '192.168.1.101'
assert ip02.adresse_suivante('192.168.255.254') == '192.168.2.0'