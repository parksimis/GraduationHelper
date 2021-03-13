/* index.js */
$(document).ready(function (){
    $("input:radio[name=double_major]").click(function (){
        if($("input[name=double_major]:checked").val() == "TRUE"){
            $("fieldset[name=hakgwa_cd]").removeAttr('disabled');
            // radio 버튼의 value 값이 1이라면 활성화

        }else if($("input[name=double_major]:checked").val() == "FALSE"){
              $("fieldset[name=hakgwa_cd]").attr("disabled",'');
            // radio 버튼의 value 값이 0이라면 비활성화
        }
    });
})


