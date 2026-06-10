var instruction = {
  stop: /^(?:stop)/i, // Arrête l’exécution du programme.
  noop: /^(?:noop|rien)/i,  // N’effectue aucune opération.
  saut: /^(?:saut|JMP) ([0-9]+)/i,  // Met le compteur à la valeur i.
  sautpos: /^(?:sautpos|JP) r([0-9]+) ([0-9]+)/i, // Si la valeur contenue dans le registre i est positive ou nulle, met le compteur à la valeur j.	
  valeur: /^(?:valeur|écrit|écriture|WR) (-{0,1}\d+) r([0-9]+)/i, // valeur x ri : Initialise le registre i avec la valeur x.
  lecture1: /^(?:lecture|copie|MOV) ([0-9]+) r([0-9]+)/i, // lecture i rj : Charge dans le registre j, le contenu de la mémoire d’adresse i.
  ecriture1: /^(?:ecriture|copie|MOV) r([0-9]+) ([0-9]+)/i, // Écrit le contenu du registre i dans la mémoire d’adresse j.
  negation: /^(?:negation|NEG) r([0-9]+)/i, // Calcule la négation du contenu du registre i.
  add: /^(?:add|addition|ADD) r([0-9]+) r([0-9]+)/i, // Ajoute la valeur du registre i à celle du registre j.
  soustr: /^(?:soustr|soust|soustraction|SUB) r([0-9]+) r([0-9]+)/i, // Soustrait la valeur du registre i à celle du registre j.
  mult: /^(?:mult|multiplication|MUL) r([0-9]+) r([0-9]+)/i,
  div: /^(?:div|division) r([0-9]+) r([0-9]+)/i,
  et: /^(?:et|AND) r([0-9]+) r([0-9]+)/i,
  ou: /^(?:ou|OR) r([0-9]+) r([0-9]+)/i,
  lecture2: /^(?:lecture|copie|MOV) \*r([0-9]+) r([0-9]+)/i, // lecture *ri rj : Charge dans le registre j, le contenu de la mémoire dont l’adresse est la valeur du registre i.
  ecriture2: /^(?:ecriture|copie|MOV) r([0-9]+) \*r([0-9]+)/i, // ecriture ri *rj : Écrit le contenu du registre i dans la mémoire dont l’adresse est la valeur du registre j.
//Instructions ajoutées
  sautnul: /^(?:sautnul|JZ) r([0-9]+) ([0-9]+)/i, // sautnul ri j : Si la valeur contenue dans le registre i est nulle, met le compteur ordinal à la valeur j.
  sautnonnul: /^(?:sautnonnul|JNZ) r([0-9]+) ([0-9]+)/i, // sautnonnul ri j : Si la valeur contenue dans le registre i est non nulle, met le compteur ordinal à la valeur j.
  lecture3: /^(?:ecriture|copie|MOV) r([0-9]+) r([0-9]+)/i,  // ecriture ri rj : Écrit le contenu du registre i dans le registre j.
  add2: /^(?:add|addition) (-{0,1}\d+) r([0-9]+)/i,
  mult2: /^(?:mult|multiplication|MUL) (-{0,1}\d+) r([0-9]+)/i,
  div2: /^(?:div|division) (-{0,1}\d+) r([0-9]+)/i,
  soustr2: /^(?:soustr|soust|soustraction|SUB) (-{0,1}\d+) r([0-9]+)/i,
  call : /^(?:appel|CALL) ([0-9]+)/i,
  ret : /^(?:retour|RET)/i,
  empiler: /^(?:empiler|PUSH) r([0-9]+)/i,
  depiler: /^(?:depiler|POP) r([0-9]+)/i,
  divent: /^(?:divent|quotient|QDV) r([0-9]+) r([0-9]+)/i, // divent ri rj : quotient de la division de la valeur du registre j par celle du registre i. (division entière)
  mod: /^(?:mod|reste|modulo) r([0-9]+) r([0-9]+)/i, // mod ri rj : reste de la division de la valeur du registre j par celle du registre i. (division entière)
  divent2: /^(?:divent|quotient|QDV) (-{0,1}\d+) r([0-9]+)/i,
  mod2: /^(?:mod|modulo) (-{0,1}\d+) r([0-9]+)/i,
  inc: /^(?:inc|incrémentation) r([0-9]+)/i, // INC ri : Incrémente la valeur du registre i de 1
  dec: /^(?:dec|décrémentation) r([0-9]+)/i // DEC ri : Décrémente la valeur du registre i de 1
};

var ri;
var cp = 1;
var mem;
var source;
var nblines=32;
var continuer = false;
// var pile = new Array(); // ajout pour call / ret
var bas_pile=0;
var last_pile=-1;
var pile_visible=false;

function split_mem() {    
    var i;
    source = $('#mem > textarea').val();
    mem = ($('#mem > textarea').val()).split('\n');
    mem = mem.map(x => x.split(";")[0].trim());
    
    $('#mem').empty();
    /*
    for (i = 1; i <= mem.length; i += 1) {
	$('#splitmem').append('<div class="ligne"><div class="numeroligne">'+i+'. </div><pre id="MEM'+i+'">'+mem[i - 1]+'</pre></div>');
    }
    */
    for (i = 0; i <= mem.length - 1; i += 1) {
        // mem[i] = mem[i].replace(/^(\s*\d*\s+)(.+)$/,'$2');
        // $('#splitmem').append('<div class="ligne"><div class="numeroligne">'+i+'. </div><pre id="MEM'+i+'">'+mem[i]+'</pre></div>');
        $('#splitmem').append('<div class="ligne"><pre id="MEM'+i+'">'+mem[i]+'</pre></div>');
    }
    $('#splitmem').bind('dblclick', edit_mem);
    $('#splitmem').show();
    if ($('#runtimenav').hasClass("limbes")) {
	$('#runtimenav').animate({left: '265'}, 500, function () {
		$('#runtimenav').removeClass("limbes");		
	  });
    }
    return false;
}

function reading(jQ) {
    jQ.addClass('read');
    setTimeout(function () {
	    jQ.removeClass('read');
	}, 500);
}

function writting(jQ) {
    jQ.addClass('wrote');
    setTimeout(function () {
	    jQ.removeClass('wrote');
	}, 500);
}

function edit_mem() {
    reset();
    //$('#mem').html('<textarea rows="'+mem.length+'">'+mem.join('\n')+"</textarea>");
    $('#mem').html('<textarea rows="'+nblines+'">'+source+"</textarea>");
    $('#mem').show();
    $('#splitmem').html('');
    $('#splitmem').hide();
    $('#mem').append('<div id="load">&nbsp;</div>');
    if(!($('#runtimenav').hasClass('limbes'))) {
	$('#runtimenav').animate({left: '-235'}, 500, function () {$('#runtimenav').addClass('limbes');});
    }
    $('#load').animate({left: '+=800'}, 500, function () {});
    $('#load').bind('click', split_mem);
}


function show_stop() {
    if (!($('#run').hasClass('limbes'))) {
	$('#run').animate({left: '-=500'}, 500, function () {
		// $('#run').hide();
	    });
//    $('#stop').show();
	$('#stop').animate({left: '+=500'}, 500, function () {
	    });
	$('#run').addClass('limbes');
    }
}
function hide_stop() {
//    $('#run').show();
    if (($('#run').hasClass('limbes'))) {
	$('#run').animate({left: '+=500'}, 500, function () {
	    });
	$('#stop').animate({left: '-=500'}, 500, function () {
//	    $('#stop').hide();
	    });
	$('#run').removeClass('limbes');
    }
}

function bus_read() {
    $('#addressbus').show();
    $('#addressbus').animate(
	{left: '320'}, 
	400, 
	function () {
	    $('#addressbus').css('left','230px');
	    $('#addressbus').hide(); 
	    $('#datasbus').show();
	    $('#datasbus').animate(
		{left: '230'}, 
		400,
		function () {
		    $('#datasbus').css('left','320px');
		    $('#datasbus').hide();
		});
	});
}

function bus_write() {
    $('#addressbus').show();
    $('#addressbus').animate(
	{left: '320'}, 
	400, 
	function () {
	    $('#addressbus').css('left','230px');
	    $('#addressbus').hide(); 
	    $('#datasbus').show();
	    $('#datasbus').addClass('writebus');
	    $('#datasbus').css('left','230px');
	    $('#datasbus').animate(
		{left: '320'}, 
		400,
		function () {
		    $('#datasbus').removeClass('writebus');
		    $('#datasbus').hide();
		});
	});
}


function finerreur() {
    $('.erreur').remove();
    $('.erreur_bus').remove();
    $('.erreur_bus2').remove();
}
function get_mem(index) {
    var chaine; 
//    if ((index <= 0) || index > mem.length) {
      if ((index < 0) || index > mem.length) {
	continuer = false;
	$('#RI').text('segmentation fault');
	/* <div class='erreur'>Erreur sur le bus d'adresse. "
         +"Il n'y a pas de case mémoire numéro "+index
         +".</div> */	
	$('body').append("<img class='erreur_bus' src='img/explosion.gif' /><img class='erreur_bus2' src='img/explosion.gif' />"); 
	$('div.erreur, img.erreur_bus, img.erreur_bus2').bind('click', finerreur);
	alert("Erreur sur le bus d'adresse. "
         +"Il n'y a pas de case mémoire numéro "+index);
	setTimeout(finerreur,1000);
	return "42";
    }
    //chaine = mem[index - 1];
    chaine = mem[index];
    return chaine;
}
function get_mem2(index) {
    bus_read();
    reading($('#MEM'+index));
    return get_mem(index);
}

function set_mem(index, chaine) {
    bus_write();
    //mem[index - 1] = chaine;
    mem[index] = chaine;
    writting($('#MEM'+index));
    $('#MEM'+index).text(chaine);
}

function set_cp(value) {
    $('#splitmem .active').removeClass('active');
    $('#MEM'+value).addClass("active");
    $('#CP').text(value);
    cp = value;
}

function get_register(num) {
    var val;
    reading($('#R'+num));
    val = parseFloat($('#R'+num).text());
    return val; /* type num */
}

function set_register(num, valeur) {
    writting($('#R'+num));
    $('#R'+num).text(valeur);
    $('#R'+num).prop('title',valeur);
}

function set_ri(str) {
    $('#RI').text(str);
}

function step() {
    // get_mem2(cp);  //Pour voir le bus a chaque chargement d'instruction
    var code = get_mem(cp);
    if (instruction.stop.test(code)) {
	set_cp(cp + 1);
	set_ri("stop");
	return false; /* <- sortie precoce */
    }
    else if (instruction.noop.test(code)) {
	set_cp(cp + 1);	
	set_ri("noop");
    }
    else if (instruction.saut.test(code)) {
	ri = instruction.saut.exec(code);
	set_cp(cp + 1);
	set_ri(ri[0]);
	set_cp(parseFloat(ri[1]));
    }
    else if (instruction.call.test(code)) {//instruction ajoutée
	ri = instruction.call.exec(code);
	set_cp(cp + 1);
	//pile.push(cp);
	set_mem(get_register(7), cp);
	set_register(7,get_register(7)-1)
	set_ri(ri[0]);
	set_cp(parseFloat(ri[1]));
	refresh_pile();
    }
    else if (instruction.ret.test(code)) {//instruction ajoutée
	ri = instruction.ret.exec(code);	
//	set_cp(pile.pop());	
	set_register(7,get_register(7)+1);
	set_cp(get_mem(get_register(7)));
	set_ri("retour");
	refresh_pile();
    }
    else if (instruction.empiler.test(code)) {//instruction ajoutée
	ri = instruction.empiler.exec(code);		
      set_cp(cp + 1);
      set_ri(ri[0]);
//	  pile.push(get_register(ri[1]));
	set_mem(get_register(7), get_register(ri[1]));
	set_register(7,get_register(7)-1)
	refresh_pile();
    }
    else if (instruction.depiler.test(code)) {//instruction ajoutée
	ri = instruction.depiler.exec(code);	
      set_cp(cp + 1);
      set_ri(ri[0]);
//      set_register(ri[1], pile.pop());
	set_register(7,get_register(7)+1);
	set_register(ri[1],get_mem(get_register(7)));
	refresh_pile();
    }
    else if (instruction.sautpos.test(code)) {
	ri = instruction.sautpos.exec(code);    
	set_cp(cp + 1);
	set_ri(ri[0]);
	if (0 <= get_register(ri[1])) {
	    writting($('#CP'));
	    set_cp(parseFloat(ri[2]));
	}
    }
    else if (instruction.sautnul.test(code)) {//instruction ajoutée
  ri = instruction.sautnul.exec(code);    
  set_cp(cp + 1);
  set_ri(ri[0]);
  if (0 == get_register(ri[1])) {
      writting($('#CP'));
      set_cp(parseFloat(ri[2]));
  }
    }
    else if (instruction.sautnonnul.test(code)) {  //instruction ajoutée
  ri = instruction.sautnonnul.exec(code);    
  set_cp(cp + 1);
  set_ri(ri[0]);
  if (0 != get_register(ri[1])) {
      writting($('#CP'));
      set_cp(parseFloat(ri[2]));
  }
    }
  else if (instruction.valeur.test(code)) {
      ri = instruction.valeur.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], ri[1]);
      if (ri[2]==7) {
	  bas_pile=ri[1];
	  reset_pile();
      }
  }
  else if (instruction.lecture1.test(code)) {
      ri = instruction.lecture1.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], parseFloat(get_mem2(parseFloat(ri[1]))));
  }
  else if (instruction.lecture2.test(code)) {
      ri = instruction.lecture2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], parseFloat(get_mem2(get_register(ri[1]))));
  }
  else if (instruction.lecture3.test(code)) { //instruction ajoutée
      ri = instruction.lecture3.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], get_register(ri[1]));
  }
  else if (instruction.ecriture1.test(code)) {
      ri = instruction.ecriture1.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_mem(parseFloat(ri[2]), get_register(ri[1]));
  }
  else if (instruction.ecriture2.test(code)) {
      ri = instruction.ecriture2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_mem(get_register(ri[2]),  get_register(ri[1]));
  }
  else if (instruction.negation.test(code)) {
      ri = instruction.negation.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[1], -get_register(ri[1]));
  }
  else if (instruction.add.test(code)) {
      ri = instruction.add.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], get_register(ri[2]) + get_register(ri[1]));
  }
  else if (instruction.add2.test(code)) {//instruction ajoutée
      ri = instruction.add2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],get_register(ri[2]) + parseInt( ri[1]));
  }
  else if (instruction.soustr.test(code)) {
      ri = instruction.soustr.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], get_register(ri[2]) - get_register(ri[1]));
  }
  else if (instruction.soustr2.test(code)) {//instruction ajoutée
      ri = instruction.soustr2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],get_register(ri[2]) - parseInt( ri[1]));
  }
  else if (instruction.mult.test(code)) {      
      ri = instruction.mult.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], get_register(ri[2]) * get_register(ri[1]));
  }
  else if (instruction.mult2.test(code)) {//instruction ajoutée
      ri = instruction.mult2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],get_register(ri[2]) * parseInt( ri[1]));
  }
  else if (instruction.div.test(code)) {
      ri = instruction.div.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2], get_register(ri[2]) / get_register(ri[1]));
  }
  else if (instruction.div2.test(code)) {//instruction ajoutée
      ri = instruction.div2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],get_register(ri[2]) / parseInt( ri[1]));
  }
  else if (instruction.divent.test(code)) {//instruction ajoutée
      ri = instruction.divent.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],(get_register(ri[2]) - (get_register(ri[2])%get_register(ri[1]))) / get_register(ri[1]));
  }
  else if (instruction.mod.test(code)) {//instruction ajoutée
      ri = instruction.mod.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],get_register(ri[2])% get_register(ri[1]));
  }
  else if (instruction.divent2.test(code)) {//instruction ajoutée
      ri = instruction.divent2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],(get_register(ri[2]) - (get_register(ri[2])% parseInt( ri[1]))) / parseInt( ri[1]));
  }
  else if (instruction.mod2.test(code)) {//instruction ajoutée
      ri = instruction.mod2.exec(code);
      set_cp(cp + 1);
      set_ri(ri[0]);
      set_register(ri[2],get_register(ri[2])% parseInt( ri[1]));
  }
  else if (instruction.inc.test(code)) {//instruction ajoutée
    ri = instruction.inc.exec(code);
    set_cp(cp + 1);
    set_ri(ri[0]);
    set_register(ri[1],get_register(ri[1])+1);
  }
  else if (instruction.dec.test(code)) {//instruction ajoutée
    ri = instruction.dec.exec(code);
    set_cp(cp + 1);
    set_ri(ri[0]);
    set_register(ri[1],get_register(ri[1])-1);
  }
  else if (instruction.et.test(code)) {//instruction ajoutée
    ri = instruction.et.exec(code);
    set_cp(cp + 1);
    set_ri(ri[0]);
    set_register(ri[1],get_register(ri[1]) && get_register(ri[2]));
  }
  else if (instruction.ou.test(code)) {//instruction ajoutée
    ri = instruction.ou.exec(code);
    set_cp(cp + 1);
    set_ri(ri[0]);
    set_register(ri[1],get_register(ri[1]) || get_register(ri[2]));
  }
  else {
      set_ri("instruction inconnue");
      /* instruction inconnue */
      return false;
  }
  return true;
}

function interactive_step () {
    if (!step()) {
	alert("fin du programme");
    }
    $('#CP').text(cp);
    return false;
}

function start_run() {
    continuer = true;
    show_stop();
    run();
}

function run() {
    if (continuer) {
	if (step()) {
	    setTimeout(run, (parseInt(document.getElementById("delai").value)+1)*100);
	} else {
	    continuer = false;
	    alert("fin du programme");
	    hide_stop();
	}
    }
    return false;
}

function stop () {
    continuer = false;
    hide_stop();
};

function reset() {
    var i;
    //set_cp(1);
    set_cp(0);
    for (i = 0; i < 8; i += 1) {
	set_register(i, 0);
    }
    reset_pile();
}

function reset_pile() {
    $("#pile").empty();
    bas_pile = get_register(7);
    last_pile=bas_pile;
}
function refresh_pile() {
    if (!pile_visible) return;
    var r7=get_register(7);    
    if (r7 < last_pile) {
	j=$('#pile').size();
	for(i = last_pile; i > r7; i--) {
	    $('#pile').prepend('<div class="ligne"><div class="numeroligne">'+i+'. </div><pre id="PILE'+j+'">'+mem[i]+'</pre></div>'); 
	    j+=1;
	}
	last_pile=r7;
    } else {
	for (i = last_pile; i < r7; i++) {
	    $('#pile > div').eq(0).remove();
	}
	last_pile=r7;
    }
}

function togglepile() {
    pile_visible = ! pile_visible;
    if (pile_visible) {
	$('#pile').show();
	$('#togglepile').html('Cacher la pile');
	refresh_pile();
    } else {
	$('#pile').hide();
	$('#togglepile').html('Voir la pile');
    }
}

function selectexemple() {
    alert('selectexemple');
}

$(document).ready(function () {
  $('#step').bind('click',interactive_step);
  $('#run').bind('click', start_run);
  $('#stop').bind('click', stop);
  $('#reset').bind('click', reset);
  $('#addressbus').hide();
  $('#datasbus').hide();
  split_mem();
  edit_mem();
  reset_pile()
  $('pile').hide();
});


