from PIL import Image
class Photo:
    def __init__(self, ima = None):
        ''' crée un objet de type Photo '''
        self.image = None
        if ima is not None:
            self.importer_image(ima)

    def creer_image(self, taille):
        ''' Crée une image
        taille: tuple: (largeur, hauteur) '''
        self.image = Image.new('RGB', (taille))
        self.taille = taille

    def importer_image(self, ima):
        ''' Importe une image dejà existante '''
        self.image = Image.open(ima)
        self.taille = self.image.size

    def recupere_pixel(self, coord):
        ''' Récupère les composantes R, V, B su pixel de coordonnées (x, y)
        coord: tuple (x, y)
        sortie: tuple (R, V, B) '''
        return (self.image.getpixel(coord))

    def depose_pixel(self, coord, couleur):
        if self.est_couleur(couleur):
            self.image.putpixel(coord, couleur)

    def coloriage(self, coordA, coordB, couleur):
        ''' Colorie le rectangle de coordonnées A -> coordB '''
        for j in range(coordA[1], coordB[1] + 1):
            for i in range(coordA[0], coordB[0] + 1):
                self.depose_pixel((i, j), couleur)

    def afficher(self):
        ''' Affiche l'objet Photo '''
        self.image.show()
    def sauver(self, nom_image):
        self.save(nom_image)
    def est_couleur(self, couleur):
        if type(couleur) != tuple or len(couleur) != 3:
            return False
        for c in couleur:
            if type(c) != int or c < 0 or c > 255:
                return False
        return True
    def en_nb(self):
        pass
    def en_daltonien(self):
        pass


im = Photo()
im.creer_image((400, 400))
im.coloriage((0, 0), (210, 210), (200, 100, 100))
#im.coloriage((0, 0), (10, 10), (100, 400, 100))
im.afficher()
