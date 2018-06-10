var cloudinary_url=	"https://api.cloudinary.com/v1_1/dalhousie-cloudcomputing/upload";
var upload_preset="t1uoork3";

var imgPreview =document.getElementById("img-preview");
var fileUpload =document.getElementById("file-upload");
//var imgUrl=document.getElementById("textinput");
var button=document.getElementById("calculate_button");

			if(fileUpload)
			{
				fileUpload.addEventListener('change',function(event)
				  {
					var file = event.target.files[0];
					console.log(file);
					var formData= new FormData();
					formData.append('file',file);
					formData.append('upload_preset',upload_preset);
					
					axios({
						url:cloudinary_url,
						method:"POST",
						headers:
						{
							'Content-Type': 'application/x-www-form-urlencoded'
							
						},
						data:formData
						}).then(function(res)
						{
							imgPreview.src=res.data.secure_url;
							console.log(res);
						}).catch(function(err)
						{
							console.error(err);
						});
						
				  });
				  
				
			}
			
function myFunction() {
    var imgUrl=document.getElementById("textinput").value;
	
	console.log("Hello!");
	console.log(imgUrl);
	
		axios({
		  method: 'get',
		  url: 'http://bit.ly/2mTM3nY',
		  responseType: 'stream'
		})
		  .then(function(response) {
		  response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
		});
	

	
}
			
			
			
