var small_pizza = document.getElementById("small");
var sum = small_pizza.getAttribute("value");
var large_pizza = document.getElementById("large");
var j = 0;
name_cust = document.getElementById("pizza_name").innerHTML;

large_pizza.onclick = setPricelarge;
small_pizza.onclick = setPricesmall;
function setPricelarge(){
         sum = large_pizza.getAttribute("value");
         topCheckbox = document.getElementsByName("top");
         for(var i = 0; i<topCheckbox.length; i++)
          {   topCheckbox[i].setAttribute(value,document.getElementById(" ").innerHTML);
              if(topCheckbox[i].checked)
              {
                  topCheckbox.checked = false;
              }
          }
        }
function setPricesmall(){
          sum = small_pizza.getAttribute("value");
          topCheckbox = document.getElementsByName("top");
          for(var i = 0; i<topCheckbox.length; i++)
          {   topCheckbox[i].setAttribute(value,document.getElementById(" ").innerHTML);
              if(topCheckbox[i].checked)
              {
                  topCheckbox[i].checked = false;
              }
          }
}
topCheckbox = document.getElementsByName("top");
for(var j = 0; j<topCheckbox.length; j++)
          {   
              topCheckbox[i].onclick = updatePrice();
          }

function updatePrice(){
        if(topCheckbox[i].checked == false)
        {
            sum = sum - topCheckbox[j].getAttribute("value");
        }
        else{
             sum = sum + topCheckbox[j].getAttribute("value");
        }
}

document.getElementById("cust").onclick = place;
function place(){
    topCheckbox = document.getElementsByName("top");
    for(var i = 0; i<topCheckbox.length; i++)
          {   
              
              if(topCheckbox[i].checked)
              {
                name_cust = name_cust + topCheckbox[i].innerHTML
              }
          }
}
document.getElementById("order").setAttribute(href,"{% url 'add_to_cart_customised_pizza' pk=regularpizza.pk label=1 price=sum name=name_cust %}");