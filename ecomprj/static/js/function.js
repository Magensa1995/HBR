console.log('working fine');

$("#commentForm").submit(function(e){
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(res){
            console.log("Comment Saved to DB...");

            if(res.bool == true){
                $("#review-res").html("Review added successfully")
                $(".hide-comment-form").hide()
                $(".add-review").hide()
                
                // Lấy đối tượng div có class là "edu-comment"
                let eduCommentDiv = document.createElement('.edu-comment');
                
                // Thiết lập nội dung HTML cho div
                let _html = '<div class="edu-comment">'
                    _html +='<div class="d-flex flex-start">'
                    _html +='<img class="rounded-circle shadow-1-strong mb-4" src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img%20(10).webp" alt="avatar" style="max-width: 50px;" />'
                    _html +='</div>'
                    _html +='<div class="comment-content">'
                    _html +='<div class="comment-top">'
                    _html +='<h6 class="title">'+ res.context.user +'</h6>'
                    _html +='<div class="rating">'

                    for (let i=1; i<=res.context.rating; i++){
                        _html +='<i class="fa fa-star" aria-hidden="true"></i>'
                    }

                    _html +='</div>'
                    _html +='</div>'
                    _html +='<p class="mb-0">'+ res.context.datetime_created +'</p>'
                    _html +='<p class="mb-0">'+ res.context.review +'</p>'
                    _html +='</div>'
                    _html +='</div>'

                // Kiểm tra xem đối tượng có tồn tại hay không
                if (eduCommentDiv) {
                    // Thiết lập nội dung HTML cho đối tượng
                    eduCommentDiv.innerHTML = _html;
                } else {
                    console.error("Element with class 'edu-comment' not found.");
                }
                // Chọn phần tử với class "container" và thêm newDiv vào đó
                let container_comment = document.querySelector('.container-comment');
                container_comment.appendChild(eduCommentDiv);

            }
        },
    })
});

function updateDateTime() {
    // Get the current date and time
    var currentDateTime = new Date();

    // Format the date and time as a string
    var dateTimeString = currentDateTime.toLocaleString();

    // Display the date and time in the specified HTML element
    document.getElementsByClassName("subtitle").innerText = dateTimeString;
}


$(".add-to-cart-btn").on("click", function(){
    let quantity = $("#pro-qty").val()
    let pro_title = $(".product_title").val()
    let pro_id = $(".product-id").val()
    let pro_price = $(".current-product-price").text()

    let this_val = $(this)

    console.log("Quantity", quantity)
    console.log("ID", pro_id)
    console.log("Title", pro_title)
    console.log("Price", pro_price)
    console.log("This is", this_val)

    $.ajax({
        url:'/add-to-cart',
        data:{
            'id':pro_id,
            'qty':quantity,
            'title':pro_title,
            'price':pro_price

        }
    })
})