//create a cache to store the users recent searches


async function getInputValue(){
        
    try{
        let query=document.getElementById("input")
        console.log(query.value)

        if (query.value===null){
            let element=document.getElementById("mess")
            element.style.display="block"
        }


        let reponse=await fetch('http://127.0.0.1:5000/',{
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "query": query.value
              }),
            })
            
            const data=await reponse.json()
            localStorage.setItem("key",JSON.stringify(data))
            localStorage.setItem("keys",query.value)

            window.location.href="http://127.0.0.1:5500/ui/result.html"
            
        console.log("success")
        
        
        
    }catch(e){
        console.log(e)
    }
        
        
}


const displayResults=()=>{

   const data=JSON.parse(localStorage.getItem("key"))
   const query=localStorage.getItem("keys")
   console.log(data)
   console.log(query)

   document.getElementsByClassName("response")[0].textContent=query

   function getLinks(object){
    return object["metadata"]["link"]

   }

   
   const listLinks=data.map(getLinks)
   console.log(listLinks)

   const movieElements = document.getElementsByClassName("movies")[0].children;

   for (let i = 0; i < listLinks.length; i++) {
    movieElements[i].textContent = listLinks[i];
 
}


//    for(let i=0; i<listLinks.length; i++){
//     document.getElementsByClassName("movie"+i.toString()).textContent=listLinks[i]
//     console.log("movie"+i.toString())
//     console.log(document.getElementsByClassName("movie"+i.toString()).textContent)
//    }



   
}






