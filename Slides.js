function Show_Element(element,display)
{
    element.style.display = display;
}
                          
function Hide_Element(element)
{
    element.style.display = 'none';
}
                          
function Show_Elements(elements,display)
{
    for (var n = 0; n < elements.length; n++)
    {
        Show_Element(elements[n],display);
    }
}

function Hide_Elements(elements) {
    Show_Elements(elements,'none');
}

function Show_Element_By_ID(elementid,display)
{
    var element = document.getElementById(elementid);
    Show_Element(element,display);
}

function Hide_Element_By_ID(elementid)
{
    var element = document.getElementById(elementid);
    Hide_Element(element);
}

function Hide_Elements_By_ID(elementids)
{
    for (var n = 0; n < elementids.length; n++)
    {
        Hide_Element_By_ID(elementids[n]);
    }
}

function Toggle_Element_By_ID(elementid,display)
{
    var element = document.getElementById(elementid);
    
    if (element.style.display=="none")
    {
        Show_Element(element,display);
    }
    else
    {
        Hide_Element(element);
    }
}

function Hide_And_Show_By_ID(hideids,showids,display='inline')
{
    for (var n = 0; n < showids.length; n++)
    {
        Show_Element_By_ID(showids[n],display);
    }
    
    for (var n = 0; n < hideids.length; n++)
    {
        Hide_Element_By_ID(hideids[n]);
    }
    
}




function Show_Elements_By_Class(classid,display)
{
    var elements = document.getElementsByClassName(classid);
    console.log("Showing",classid,display,elements.length);
    Show_Elements(elements,display);
}

function Hide_Elements_By_Class(classid)
{
    var elements = document.getElementsByClassName(classid);
    console.log("Hiding",classid,elements.length);
    
    Show_Elements(elements,"none");
}


function Toggle_Class(classid,display)
{
    var elements = document.getElementsByClassName(classid);

    var hidden=0;
    var show=0;
    for (var n = 0; n < elements.length; n++)
    {
        if (elements[n].style.display=='none')
        {
            elements[n].style.display=display;
            show++;
        }
        else
        {
            elements[n].style.display='none';
            hidden++;
        }

    }
}
