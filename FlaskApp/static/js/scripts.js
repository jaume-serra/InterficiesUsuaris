function toggle(carta) {
    carta = '#' + carta
    if (document.querySelector(carta).style.display == "block") {
        document.querySelector(carta).style.display = "none";
    }
    else {
        document.querySelector(carta).style.display = "block";
    }
}


function add_product(plate, price) {
    var section_name = plate + "Section";
    var id_n = "n-" + plate;
    var path = document.getElementById("basket-products");
    var id_price = "p-" + plate;

    if (document.getElementById(section_name)) {
        up(id_n, '10', id_price);
        return;
    }

    var new_product = document.createElement("section");
    new_product.setAttribute("id", section_name);
    new_product.classList.add("w3-display-container", "w3-padding-16", "w3-panel", "w3-border-top", "w3-border-black")
    path.appendChild(new_product);

    var plt = document.createElement("span");
    var txt1 = document.createTextNode(plate);
    plt.appendChild(txt1);
    plt.classList.add("w3-display-left");
    document.getElementById(section_name).appendChild(plt);

    var prc = document.createElement("span");
    var txt2 = document.createTextNode(parseInt(price));

    prc.setAttribute("id", id_price);
    prc.setAttribute("data-price", price);
    prc.appendChild(txt2);
    prc.classList.add("w3-display-right", "money", "product-price");
    document.getElementById(section_name).appendChild(prc);

    var div1 = document.createElement("div");
    div1.classList.add("input-group", "w3-display-middle");
    document.getElementById(section_name).appendChild(div1);

    var div2 = document.createElement("div");
    div2.classList.add("input-group-btn");
    div1.appendChild(div2);

    var inpt = document.createElement("input");
    inpt.setAttribute("id", id_n);
    inpt.value = 1;
    inpt.classList.add("input-number");
    div1.appendChild(inpt);

    var div3 = document.createElement("div");
    div3.classList.add("input-group-btn");
    div1.appendChild(div3);

    var btn1 = document.createElement("button");
    btn1.appendChild(document.createTextNode('-'));
    btn1.classList.add("btn");
    btn1.onclick = function () { down(id_n, '1', id_price); };
    div2.appendChild(btn1);

    var btn2 = document.createElement("button");
    btn2.appendChild(document.createTextNode('+'));
    btn2.classList.add("btn");
    btn2.onclick = function () { up(id_n, '10', id_price); };
    div3.appendChild(btn2);

    var trsh = document.createElement("i");
    trsh.classList.add("fa", "fa-trash", "trash");
    trsh.onclick = function () { delete_product(section_name); };
    document.getElementById(section_name).appendChild(trsh);

    console.log('div1 :>> ', div1);
    // const product = {"id":id_price, "price":price}
    update_total_price();
}


function delete_product(plate) {
    const element = document.getElementById(plate);
    element.remove();
    update_total_price()
}

function up(id, max, id_price) {
    document.getElementById(id).value = parseInt(document.getElementById(id).value) + 1;
    if (document.getElementById(id).value > parseInt(max)) {
        document.getElementById(id).value = max;
    }
    else
        update_local_price(id_price, id);
}
function down(id, min, id_price) {
    document.getElementById(id).value = parseInt(document.getElementById(id).value) - 1;
    if (document.getElementById(id).value < parseInt(min)) {
        document.getElementById(id).value = min;
    }
    else
        update_local_price(id_price, id);
}

function update_local_price(id_price, id_n) {
    var price = parseFloat(document.getElementById(id_price).getAttribute('data-price'));
    var n = parseInt(document.getElementById(id_n).value);
    document.getElementById(id_price).textContent = (n * price).toFixed(2);
    update_total_price();
}

function update_total_price() {
    var sum = 0;
    var c = document.getElementsByClassName("product-price");
    for (var i = 0; i < c.length; i++) {
        sum = sum + parseFloat(c[i].textContent);
    }
    document.getElementById("total-price").textContent = sum.toFixed(2);
}

