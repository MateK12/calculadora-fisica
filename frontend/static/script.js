let fila_cont = document.getElementById("fila_cont");
let friccion_input = document.getElementById("friccion_I");
let friccion_si = document.getElementById("friccion_si");
let friccion_no = document.getElementById("friccion_no");
let angulo_input = document.getElementById("angulo_input");
let masa_input = document.getElementById("masa_input");
let fuerza_input = document.getElementById("fuerza_input");
let select_pni = document.getElementById("select_pni");
let cont_pni = document.getElementById("cont_pni");
let calcular = document.getElementById("bot_alcular");
mensaje_back = {
    "plano":0,
    "angulo":0,
    "masa":0,
    "fuerza":0,
    "existencia_friccion":0,
    "materiales":0,
    "friccion_estatica":0,
    "friccion_dinamica":0,
    "que_calcular":0,
    "aceleracion":0,
}

let opciones = ["Madera sobre madera","Acero sobre hielo","Teflón sobre teflón","Caucho sobre cemento seco","Vidrio sobre vidrio","Esquí sobre nieve",
"Madera sobre cuero","Aluminio sobre acero","Madera sobre cuero","Articulaciones humanas","Personalizado"]
let angulo = 0
let masa = 0
let fuerza = 0
let E_friccion = 0
let material = 0
let friccion_estatica = 0
let friccion_dianamica = 0 

angulo_input.addEventListener("blur",()=>{
    angulo = angulo_input.value
    i = parseInt(angulo)
    mensaje_back.angulo = i
})
masa_input.addEventListener("blur",()=>{
    masa = masa_input.value
    i = parseInt(masa)
    mensaje_back.masa = i

})
fuerza_input.addEventListener("blur",()=>{
    fuerza = fuerza_input.value
    i = parseInt(fuerza)
    mensaje_back.fuerza = i

})

friccion_si.addEventListener("click",()=>{
    mensaje_back.plano =1
    mensaje_back.existencia_friccion =1;
    let cont_friccion = document.getElementById("cont_friccion")
    cont_friccion.innerHTML = `<select class="form-select" id="select_materiales">
    <option value=1>Madera sobre madera</option>
    <option value=2>Acero sobre hielo</option>
    <option value=3 >Teflón sobre teflón</option>
    <option value=4 >Caucho sobre cemento seco</option>
    <option value=5 >Vidrio sobre vidrio</option>
    <option value=6 >Esquí sobre nieve</option>
    <option value=7 >Madera sobre cuero</option>
    <option value=8 >Aluminio sobre acero</option>
    <option value=9 >Articulaciones humanas</option>
    <option value=10 >Personalizado</option>  
  </select>`
    select = document.getElementById("select_materiales");
   
    select.addEventListener("blur",()=>{
        let valor_select = document.getElementById("select_materiales").value;
        p = parseInt(valor_select)
        mensaje_back.materiales = p
        if(valor_select == 10){
            let cont_fricciones = document.getElementById("cont_fricciones1");
            cont_fricciones.innerHTML=`<label class="col-form-label mt-4" for="inputDefault">Friccion dinamica (Número entre 0 y 1 usar .)</label>
                                        <input type="text" class="form-control" placeholder="numero entre 0 y 1" id="f_dinamica">
                                        <label class="col-form-label mt-4" for="inputDefault">Friccion estatica (Número entre 0 y 1 usar .)</label>
                                        <input type="text" class="form-control" placeholder="numero entre 0 y 1" id="f_estatica">`
            let dinamica = document.getElementById("f_dinamica");
            let estatica = document.getElementById("f_estatica");
            dinamica.addEventListener("blur",()=>{
                friccion_dianamica = dinamica.value;
                i = parseFloat(friccion_dianamica);
                mensaje_back.friccion_dinamica = i
            })
            estatica.addEventListener("blur",()=>{
                friccion_estatica = estatica.value
                i = parseFloat(friccion_estatica)
                mensaje_back.friccion_estatica = i
            })
        }
    })
    
})
friccion_no.addEventListener("click",()=>{
    mensaje_back.existencia_friccion =2

})
select_pni.addEventListener("blur",()=>{
    let val_sel = document.getElementById("select_pni").value;
    i = parseInt(val_sel);
    mensaje_back.que_calcular = i;
    if(val_sel == 1){
        mensaje_back.plano = 2
        cont_pni.innerHTML=`  <div class="form-group">
        <label class="col-form-label mt-4" for="inputDefault"><h4>Fuerza</h4></label>
        <input type="text" class="form-control" placeholder="fuerza" id="fuerza_input_pni">                        
       <label class="col-form-label mt-4" for="inputDefault"><h4>Aceleracion</h4></label>
        <input  type="text" class="form-control" placeholder="Aceleracion" id="aceleracion">
    </div>`
    let fuerza_input_pni = document.getElementById("fuerza_input_pni");
    fuerza_input_pni.addEventListener("blur",()=>{
        let fue = fuerza_input_pni.value;
        i = parseFloat(fue);
        mensaje_back.fuerza = i;
    })
    let aceleracion = document.getElementById("aceleracion");
    aceleracion.addEventListener("blur",()=>{
        let fue = aceleracion.value;
        i = parseFloat(fue);
        mensaje_back.aceleracion = i;
    
    })}
    if (val_sel==2) {
        mensaje_back.plano = 2
        cont_pni.innerHTML=`  <div class="form-group">
        <label class="col-form-label mt-4" for="inputDefault"><h4>Masa</h4></label>
        <input  type="text" class="form-control" placeholder="masa" id="masa_input_pni">
        <label class="col-form-label mt-4" for="inputDefault"><h4>Aceleracion</h4></label>
        <input  type="text" class="form-control" placeholder="Aceleracion" id="aceleracion">
    </div>`
    let masa_pni = document.getElementById("masa_input_pni");
    masa_pni.addEventListener("blur",()=>{
        let fue = masa_pni.value;
        i = parseFloat(fue);
        mensaje_back.masa = i;
    })
    let aceleracion = document.getElementById("aceleracion");
    aceleracion.addEventListener("blur",()=>{
        let fue = aceleracion.value;
        i = parseFloat(fue);
        mensaje_back.aceleracion = i;
    
    })}
    
    if (val_sel==3) {
        mensaje_back.plano = 2
        cont_pni.innerHTML=`  <div class="form-group">
        <label class="col-form-label mt-4" for="inputDefault"><h4>Masa</h4></label>
        <input  type="text" class="form-control" placeholder="masa" id="masa_input_pni">
        <label class="col-form-label mt-4" for="inputDefault"><h4>Fuerza</h4></label>
        <input type="text" class="form-control" placeholder="fuerza" id="fuerza_input_pni"> 
        <label class="col-form-label mt-4" for="inputDefault"><h4>¿Hay friccion?</h4></label> 
        <button type="button" id="friccion_si_pni" class="btn btn-primary" >Si</button>
        <button type="button" id="friccion_no_pni" class="btn btn-primary">No</button>
        <div id="cont_sel"></div>
        </div>`
        let friccion_no_pni = document.getElementById("friccion_no_pni");
        friccion_no_pni.addEventListener("click",()=>{
            mensaje_back.existencia_friccion =2
            mensaje_back.plano =2
        })
        let fuerza_input_pni = document.getElementById("fuerza_input_pni");
        let masa_pni = document.getElementById("masa_input_pni");
        fuerza_input_pni.addEventListener("blur",()=>{
            let fue = masa_pni.value;
            i = parseFloat(fue);
            mensaje_back.masa = i;
        })
        fuerza_input_pni.addEventListener("blur",()=>{
            let fue = fuerza_input_pni.value;
            i = parseFloat(fue);
            mensaje_back.fuerza = i;
        })
        let friccion_si_pni = document.getElementById("friccion_si_pni");
        let cont_sel = document.getElementById("cont_sel");
        let html_select = ` <label for="exampleSelect1" class="form-label mt-4">Materiales</label>
        <select class="form-select" id="select_materiales_pni">
          <option value=1>Madera sobre madera</option>
          <option value=2>Acero sobre hielo</option>
          <option value=3 >Teflón sobre teflón</option>
          <option value=4 >Caucho sobre cemento seco</option>
          <option value=5 >Vidrio sobre vidrio</option>
          <option value=6 >Esquí sobre nieve</option>
          <option value=7 >Madera sobre cuero</option>
          <option value=8 >Aluminio sobre acero</option>
          <option value=9 >Articulaciones humanas</option>
          <option value=10 >Personalizado</option>  
        </select>
        <div id="conte_pni"></div>
        `

        friccion_si_pni.addEventListener("click",()=>{
                mensaje_back.existencia_friccion =1;
                mensaje_back.plano =2
                cont_sel.innerHTML = html_select;
                let select_materiales_pni = document.getElementById("select_materiales_pni")
                select_materiales_pni.addEventListener("blur",()=>{
                    let valor_select1 = document.getElementById("select_materiales_pni").value;
                    mensaje_back.materiales = parseInt(valor_select1)
                    if(valor_select1 == 10){
                        let conte_pni = document.getElementById("conte_pni");
                        conte_pni.innerHTML=`<label class="col-form-label mt-4" for="inputDefault">Friccion dinamica (Número entre 0 y 1 usar .)</label>
                                                    <input type="text" class="form-control" placeholder="fricción dinamica 0 y 1" id="f_dinamica">
                                                    <label class="col-form-label mt-4" for="inputDefault">Friccion estatica (Número entre 0 y 1 usar .)</label>
                                                    <input type="text" class="form-control" placeholder="fricción estatica" id="f_estatica">`
                        // fila_cont.appendChild(cont_fricciones)
                        let dinamica = document.getElementById("f_dinamica");
                        let estatica = document.getElementById("f_estatica");
                        dinamica.addEventListener("blur",()=>{
                            friccion_dianamica = dinamica.value;
                            i = parseFloat(friccion_dianamica);
                            mensaje_back.friccion_dinamica = i
                        })
                        estatica.addEventListener("blur",()=>{
                            friccion_estatica = estatica.value
                            i = parseFloat(friccion_estatica)
                            mensaje_back.friccion_estatica = i
                        })
                    }
                })
               
            })
            
        }
    }
)
let cont_resultados = document.getElementById("cont_resultados")
console.log(mensaje_back)
let API = "http://localhost:5000"
const envio_datos = async (e)=>{
    console.log("kkkk")
    const respuesta = await fetch(`${API}/calcular`,{
      method:"POST",
      headers:{"Content-Type":"application/json"
    },
    body: JSON.stringify(mensaje_back)
    })
    const data = await respuesta.json();
    console.log(data)
    for (let i = 0; i < data.mensaje.length; i++) {
        console.log(data.mensaje.length)
        let br = document.createElement("br")
        cont_resultados.innerHTML =data.mensaje
        cont_resultados.appendChild(br)
    }  }
const envio_datos_PNI = async (e)=>{
    console.log("kkkk")
    const respuesta = await fetch(`${API}/calcular_PNI`,{
      method:"POST",
      headers:{"Content-Type":"application/json"
    },
    body: JSON.stringify(mensaje_back)
    })
    const data = await respuesta.json();
    console.log(data.mensaje)
    for (let i = 0; i < data.mensaje.length; i++) {
       
        cont_resultados.innerHTML = data.mensaje

    }

  }
calcular.addEventListener("click",envio_datos)
let calcula_PNI = document.getElementById("calcular_PNI");
calcula_PNI.addEventListener("click",envio_datos_PNI)