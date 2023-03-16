class etudiant:
    def __init__(self, p_prenom, p_nom, p_num, p_vip:bool, p_danger:bool) -> None:
        self.prenom = p_prenom
        self.nom = p_nom
        self.num = p_num
        self.vip = p_vip
        self.danger = p_danger
    
    def __str__(self) -> str:
        return f"""
------------------------------
Prenom: {self.prenom}
Nom: {self.nom}
Numero: {self.num}
V.I.P: {self.vip}
Danger: {self.danger}
------------------------------
        """