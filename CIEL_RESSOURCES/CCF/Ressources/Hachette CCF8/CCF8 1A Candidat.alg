<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="FIN_ALGORITHME" texte="Algorithme de M. Joyeux"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2para="" F2lignes="" F2defaut="" F2etat="inactif"/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="n EST_DU_TYPE NOMBRE" code="1#NOMBRE#n"/>
        <item algoitem="U EST_DU_TYPE NOMBRE" code="1#NOMBRE#U"/>
        <item algoitem="C EST_DU_TYPE NOMBRE" code="1#NOMBRE#C"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="n PREND_LA_VALEUR 0" code="5#n#0#pasliste"/>
        <item algoitem="U PREND_LA_VALEUR ??????" code="5#U#??????#pasliste"/>
        <item algoitem="C PREND_LA_VALEUR 390015.91" code="5#C#390015.91#pasliste"/>
        <item algoitem="TANT_QUE (U>C) FAIRE" code="15#U>C">
            <item algoitem="DEBUT_TANT_QUE" code="16#debuttantque"/>
            <item algoitem="U PREND_LA_VALEUR ??????" code="5#U#??????#pasliste"/>
            <item algoitem="C PREND_LA_VALEUR ???????" code="5#C#???????#pasliste"/>
            <item algoitem="n PREND_LA_VALEUR n+1" code="5#n#n+1#pasliste"/>
            <item algoitem="FIN_TANT_QUE" code="17#fintantque"/>
        </item>
        <item algoitem="AFFICHER n" code="3#n#0#pasliste"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
