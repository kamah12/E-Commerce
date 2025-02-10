// $(document).ready(function () {

//     $('.increment-btn').click(function (e) { 
//         e.preventDefault();
//         var increment_value = $(this).closest('.product_data').find('.qty-input').val();
//         var value = parseInt(increment_value,10);
//         value = isNaN(value) ? 0 : value;
//         if(value < 0)
//         {
//             value++;
//             $(this).closest('.product_data').find('.qty-input').val(value);
//         }
//     });

//     $('.decrement-btn').click(function (e) { 
//         e.preventDefault();
//         var increment_value = $(this).closest('.product_data').find('.qty-input').val();
//         var value = parseInt(increment_value,10);
//         value = isNaN(value) ? 0 : value;
//         if(value > 1)
//         {
//             value--;
//             $(this).closest('.product_data').find('.qty-input').val(value);
//         }
//     }); 

//     $('.addBtnToCart').click(function (e) { 
//         e.preventDefault();
//         var product_id = $(this).closest('.product_data').find('.prodId').val();
//         var product_qty = $(this).closest('.product_data').find('.qty-input').val();
//         var token = $('input[name=csrfmiddlewaretoken]').val();
//         $.ajax({
//             method: "POST",
//             url: "/add-to-cart",
//             data: {
//                 'product_id': product_id,
//                 'product_qty': product_qty,
//                 csrfmiddlewaretoken: token
//             },
//             success: function (response) {
//                 console.log(response)
//                 alertify.success(response)
//             }
//         });
//     });
// });

$(document).ready(function () {

    // Increment button logic
    $('.increment-btn').click(function (e) { 
        e.preventDefault();

        var current_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(current_value, 10);
        value = isNaN(value) ? 0 : value;

        
        var max_stock = 10; 
        if (value < max_stock) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        } 
    });

    // Decrement button logic
    $('.decrement-btn').click(function (e) { 
        e.preventDefault();

        var current_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(current_value, 10);
        value = isNaN(value) ? 0 : value;

        // Prevent decrement below 1
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        } 
    }); 

    // Add to cart button logic
    $('.addBtnToCart').click(function (e) { 
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prodId').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status); 
            },
        });
    });

    // update products to cart 
    $('.changeQuantity').click(function (e) { 
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prodId').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                // console.log(response);
                // alertify.success(response.status); 
            },
        });
    });

    // remove products from cart 
    $('.remove-from-cart').click(function (e) { 
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prodId').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/remove-from-cart",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);  
                $('.cartdata').load(location.href + ' .cartdata');
            },
        });
        
    });

    // Add to Wishlist button logic
    $('.addToWishlist').click(function (e) { 
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prodId').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);  
            },
        });

    });

    // remove products from wishlist 
    $('.remove-from-wishlist').click(function (e) { 
        e.preventDefault();
        
        var product_id = $(this).closest('.product_data').find('.prodId').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/remove-from-wishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);  
                $('.wishdata').load(location.href + ' .wishdata');
            },
        });
        
    });
    
});

//show navbar after scroll
// window.addEventListener("scroll",(e)=>{
//     console.log(this.pageYOffset);
//     if (this.pageYOffset>60) {
//         document.querySelector(".navbar").classList.add("show");
//     }
//     else{
//         document.querySelector(".navbar").classList.remove("show");

//     }
// });
