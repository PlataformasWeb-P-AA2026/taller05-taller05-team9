import './style.css';
import DataTable from 'datatables.net-dt';
import 'datatables.net-dt/css/dataTables.dataTables.css';

const BASE_URL = "http://localhost:5985/jugadores/_design/losjugadores/_view/";

let tabla = null;

async function cargarDatos(vista = "por_club") {
  try {
    const respuesta = await fetch(`${BASE_URL}${vista}`);
    
    if (!respuesta.ok) {
      throw new Error("Error al consumir la API");
    }

    const json = await respuesta.json();

    const datos = json.rows.map(row => {
      return {
        criterio: row.key,
        nombre: row.value.nombre,
        club: row.value.club_actual,
        posicion: row.value.posicion,
        goles: row.value.goles,
        partidos: row.value.partidos,
        seleccion: row.value.seleccion
      };
    });

    if (tabla) {
      tabla.destroy();
      document.querySelector("#tabla-posts").innerHTML = "";
    }

    tabla = new DataTable("#tabla-posts", {
      data: datos,
      columns: [
        { data: "criterio", title: "Criterio" },
        { data: "nombre", title: "Nombre" },
        { data: "club", title: "Club" },
        { data: "posicion", title: "Posición" },
        { data: "goles", title: "Goles" },
        { data: "partidos", title: "Partidos" },
        { data: "seleccion", title: "Selección" }
      ],
      pageLength: 10,
      language: {
        search: "Filtrar resultados:",
        lengthMenu: "Mostrar _MENU_",
        info: "Total: _TOTAL_ registros",
        paginate: { previous: "Ant.", next: "Sig." }
      }
    });

  } catch (error) {
    console.error("Error:", error);
  }
}

document.getElementById("vista").addEventListener("change", function() {
  cargarDatos(this.value);
});

cargarDatos();
