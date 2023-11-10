function  func_pop_up(){
    document.getElementById("pop_up").style.display = "block";
    const addCSS = css => document.head.appendChild(document.createElement("style")).innerHTML=css;

    addCSS(".container{ filter: blur(10px); }");

};
function back(){
    document.getElementById("pop_up").style.display = "none"
    const addCSS = css => document.head.appendChild(document.createElement("style")).innerHTML=css;

    addCSS(".container{ filter: blur(0px); }");
};

function ChangeTheme(){
    var link = document.getElementById("theme-link");
    let lightTheme = "light.css";
    let darkTheme = "dark.css";
    
    var currTheme = link.getAttribute("href");
    var theme = "";

    if(currTheme == lightTheme)
    {
   	 currTheme = darkTheme;
   	 theme = "dark";
    }
    else
    {    
   	 currTheme = lightTheme;
   	 theme = "light";
    }

    link.setAttribute("href", currTheme);


};