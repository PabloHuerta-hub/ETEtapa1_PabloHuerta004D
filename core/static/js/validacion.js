function validacion() {
  title = document.getElementById("titulo").value;
  categoria = document.getElementById("categoria").value;
  urls = document.getElementById("urls").value;
  info = document.getElementById("info").value;
  if (title == null || title.length == 0 || /^\s+$/.test(title)) {
    alert("Debe ingresar un titulo");
    document.getElementById("titulo").value = "";
    document.datos.title.focus();
    return false;
  }

  if (categoria == null || categoria.length == 0 || /^\s+$/.test(categoria)) {
    alert("Debe elegir una categoria");
    document.getElementById("categoria").value = "";
    document.datos.categoria.focus();
    return false;
  }

  if (urls == null || urls.length == 0 || /^\s+$/.test(urls)) {
    alert("Debe ingresar una urls");
    document.getElementById("urls").value = "";
    document.datos.urls.focus();
    return false;
  }

  if (info == null || info.length == 0 || /^\s+$/.test(info)) {
    alert("Debe ingresar una descripcion valida");
    document.getElementById("info").value = "";
    document.datos.info.focus();
    return false;
  }
  return alert("Se ha registrado tu noticia");
}
