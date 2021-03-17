/* index.js */

$(document).ready(function (){
    $("input:radio[name=double_major]").click(function (){
        if($("input[name=double_major]:checked").val() == "TRUE"){
            $("fieldset[name=hakgwa_cd]").removeAttr('disabled');
            // radio 버튼의 value 값이 TRUE(==복수전공) 이라면 활성화

        }else if($("input[name=double_major]:checked").val() == "FALSE"){
              $("fieldset[name=hakgwa_cd]").attr("disabled",'');
            // radio 버튼의 value 값이 FALSE(== 단일전공)이라면 비활성화
        }
    });

})


var major = {"rows":[
                {"id":1,"kname":"▶진성애교양대학","up":"A1200","div":"A","display_order":"111010X","ename":"▶","code":"A1216"},
                {"id":2,"kname":"▶인문대학","up":"A1200","div":"A","display_order":"11A1000","ename":"▶","code":"A1470"},
                {"id":3,"kname":"▶예술체육대학","up":"A1200","div":"A","display_order":"11A1001","ename":"▶","code":"A1480"},
                {"id":4,"kname":"▶지식정보서비스대학","up":"A1200","div":"A","display_order":"11A2000","ename":"▶College of Knowledge Information and Service","code":"A1430"},
                {"id":5,"kname":"▶사회과학대학","up":"A1200","div":"A","display_order":"11A2A00","ename":"▶College of Social Sciences","code":"A1435"},
                {"id":6,"kname":"▶소프트웨어경영대학","up":"A1200","div":"A","display_order":"11A2B00","ename":"▶","code":"A1455"},
                {"id":7,"kname":"▶융합과학대학","up":"A1200","div":"A","display_order":"11A3000","ename":"▶College of Convergence and Integrated Science","code":"A1450"},
                {"id":8,"kname":"▶창의공과대학","up":"A1200","div":"A","display_order":"11A4000","ename":"▶College of Creative Engineering","code":"A1440"},
                {"id":9,"kname":"▶창의공과대학","up":"A2200","div":"A","display_order":"12A4000","ename":"▶College of Creative Engineering","code":"A2440"},
                {"id":10,"kname":"▶진성애교양대학","up":"A4200","div":"A","display_order":"13A0101","ename":"▶","code":"A4216"},
                {"id":11,"kname":"▶소프트웨어경영대학","up":"A4200","div":"A","display_order":"13A0501","ename":"▶","code":"A4455"},
                {"id":12,"kname":"▶관광문화대학","up":"A4200","div":"A","display_order":"13A5000","ename":"▶College of Tourism and Culture","code":"A4460"},
                {"id":13,"kname":"▶교직학부","up":"A1216","div":"B","display_order":"11A0200","ename":"▶Division of Teacher Education","code":"0019E"},
                {"id":14,"kname":"ROTC","up":"A1216","div":"B","display_order":"11A0X91","ename":"","code":"Z0003"},
                {"id":15,"kname":"유아교육과","up":"A1470","div":"B","display_order":"11A1110","ename":"Early Childhood Education","code":"81046"},
                {"id":16,"kname":"국어국문학과","up":"A1470","div":"B","display_order":"11A1210","ename":"Department of Korean Language & Literature","code":"80101"},
                {"id":17,"kname":"영어영문학과","up":"A1470","div":"B","display_order":"11A1220","ename":"Department of English Language & Literature","code":"80102"},
                {"id":18,"kname":"중어중문학과","up":"A1470","div":"B","display_order":"11A1230","ename":"Department of Chinese Language & Literature","code":"80108"},
                {"id":19,"kname":"사학과","up":"A1470","div":"B","display_order":"11A1240","ename":"Department of History","code":"80106"},
                {"id":20,"kname":"문헌정보학과","up":"A1470","div":"B","display_order":"11A1250","ename":"Department of Library & Information Science","code":"80107"},
                {"id":21,"kname":"문예창작학과","up":"A1470","div":"B","display_order":"11A1260","ename":"Department of Creative Writing","code":"81001"},
                {"id":22,"kname":"▶글로벌어문학부","up":"A1470","div":"B","display_order":"11A1300","ename":"▶Division of Global Language and Literature","code":"0A220"},
                {"id":23,"kname":"서양화ㆍ미술경영학과","up":"A1480","div":"B","display_order":"11A1410","ename":"Department of Western Painting and Art Management","code":"81047"},
                {"id":24,"kname":"한국화ㆍ서예학과","up":"A1480","div":"B","display_order":"11A1420","ename":"Department of Korean Painting and Calligraphy","code":"81048"},
                {"id":25,"kname":"입체조형학과","up":"A1480","div":"B","display_order":"11A1430","ename":"Department of Ceramic Art and Sculpture","code":"81049"},
                {"id":26,"kname":"▶디자인비즈학부","up":"A1480","div":"B","display_order":"11A1500","ename":"▶Division of Design Business","code":"0A240"},
                {"id":27,"kname":"▶Fine Arts학부","up":"A1480","div":"B","display_order":"11A15A0","ename":"▶","code":"0A260"},
                {"id":28,"kname":"▶스포츠과학부","up":"A1480","div":"B","display_order":"11A1600","ename":"▶Division of Sports Science","code":"0A250"},
                {"id":29,"kname":"시큐리티매니지먼트학과","up":"A1480","div":"B","display_order":"11A1650","ename":"","code":"81039"},
                {"id":30,"kname":"체육학과","up":"A1480","div":"B","display_order":"11A1710","ename":"Department of Physical Education","code":"80701"},
                {"id":31,"kname":"법학과","up":"A1430","div":"B","display_order":"11A2110","ename":"Department of Law","code":"81040"},
                {"id":32,"kname":"행정학과","up":"A1430","div":"B","display_order":"11A2120","ename":"Department of Public Administration","code":"80202"},
                {"id":33,"kname":"경찰행정학과","up":"A1430","div":"B","display_order":"11A2130","ename":"Department of Police Administration","code":"81004"},
                {"id":34,"kname":"▶휴먼서비스학부","up":"A1430","div":"B","display_order":"11A2200","ename":"▶Division of Human Services","code":"0A320"},
                {"id":35,"kname":"국제관계학과","up":"A1430","div":"B","display_order":"11A2310","ename":"Department of International Relations","code":"81042"},
                {"id":36,"kname":"국제산업정보학과","up":"A1430","div":"B","display_order":"11A2320","ename":"Department of International Industrial Information","code":"81043"},
                {"id":37,"kname":"▶경제학부","up":"A1430","div":"B","display_order":"11A2400","ename":"▶Division of Economics","code":"0A340"},
                {"id":38,"kname":"지식재산학과","up":"A1430","div":"B","display_order":"11A2510","ename":"Department of Intellectual Property","code":"81007"},
                {"id":39,"kname":"경영학과","up":"A1430","div":"B","display_order":"11A2610","ename":"Department of Business Administration","code":"80302"},
                {"id":40,"kname":"무역학과","up":"A1430","div":"B","display_order":"11A2620","ename":"Department of International Trade","code":"80304"},
                {"id":41,"kname":"▶회계세무ㆍ경영정보학부","up":"A1430","div":"B","display_order":"11A2700","ename":"▶Division of Accounting and Management Information","code":"0A360"},
                {"id":42,"kname":"국제통상학과","up":"A1430","div":"B","display_order":"11A2810","ename":"International Commerce","code":"81009"},
                {"id":43,"kname":"▶공공안전학부","up":"A1435","div":"B","display_order":"11A2A10","ename":"▶","code":"0A351"},
                {"id":44,"kname":"▶공공인재학부","up":"A1435","div":"B","display_order":"11A2A20","ename":"▶","code":"0A352"},
                {"id":45,"kname":"▶경제학부","up":"A1435","div":"B","display_order":"11A2A30","ename":"▶","code":"0A353"},
                {"id":46,"kname":"▶K-WITH 융합교육원","up":"A1455","div":"B","display_order":"11A2B01","ename":"▶","code":"C1455"},
                {"id":47,"kname":"▶AI컴퓨터공학부","up":"A1455","div":"B","display_order":"11A2BA0","ename":"▶","code":"0A551"},
                {"id":48,"kname":"▶ICT융합학부","up":"A1455","div":"B","display_order":"11A2BB0","ename":"▶","code":"0A552"},
                {"id":49,"kname":"▶경영학부","up":"A1455","div":"B","display_order":"11A2BC0","ename":"▶","code":"0A553"},
                {"id":50,"kname":"수학과","up":"A1450","div":"B","display_order":"11A3110","ename":"Department of Mathematics","code":"80401"},
                {"id":51,"kname":"전자물리학과","up":"A1450","div":"B","display_order":"11A3120","ename":"Department of Electro physics","code":"81014"},
                {"id":52,"kname":"나노공학과","up":"A1450","div":"B","display_order":"11A3121","ename":"나노공학과","code":"81012"},
                {"id":53,"kname":"화학과","up":"A1450","div":"B","display_order":"11A3130","ename":"Department of Chemistry","code":"80403"},
                {"id":54,"kname":"▶바이오융합학부","up":"A1450","div":"B","display_order":"11A3200","ename":"▶Division of Bio-convergence","code":"0A520"},
                {"id":55,"kname":"컴퓨터공학부","up":"A1450","div":"B","display_order":"11A3300","ename":"Division of Computer Science and Engineering","code":"0A530"},
                {"id":56,"kname":"융합보안학과","up":"A1450","div":"B","display_order":"11A3X20","ename":"Department of Convergence Security","code":"80921"},
                {"id":57,"kname":"토목공학과","up":"A1440","div":"B","display_order":"11A4110","ename":"Department of Civil Engineering","code":"80501"},
                {"id":58,"kname":"건축학과","up":"A1440","div":"B","display_order":"11A4120","ename":"Department of Architecture","code":"81018"},
                {"id":59,"kname":"건축공학과","up":"A1440","div":"B","display_order":"11A4130","ename":"Department of Architectural Engineering","code":"80512"},
                {"id":60,"kname":"도시ㆍ교통공학과","up":"A1440","div":"B","display_order":"11A4140","ename":"Department of Urban & Transportation Engineering","code":"81022"},
                {"id":61,"kname":"산업경영공학과","up":"A1440","div":"B","display_order":"11A4210","ename":"Department of Industrial & Management Engineering","code":"81020"},
                {"id":62,"kname":"전자공학과","up":"A1440","div":"B","display_order":"11A4220","ename":"Department of Electronic Engineering","code":"80506"},
                {"id":63,"kname":"기계시스템공학과","up":"A1440","div":"B","display_order":"11A4230","ename":"Department of Mechanical System Engineering","code":"81023"},
                {"id":64,"kname":"신소재공학과","up":"A1440","div":"B","display_order":"11A4310","ename":"Department of Advanced Materials Engineering","code":"81021"},
                {"id":65,"kname":"환경에너지공학과","up":"A1440","div":"B","display_order":"11A4320","ename":"Department of Environmental Energy Engineering","code":"81037"},
                {"id":66,"kname":"화학공학과","up":"A1440","div":"B","display_order":"11A4330","ename":"Department of Chemical Engineering","code":"80509"},
                {"id":67,"kname":"▶융합에너지시스템공학부","up":"A1440","div":"B","display_order":"11A4A10","ename":"▶","code":"0A401"},
                {"id":68,"kname":"▶스마트시티공학부","up":"A1440","div":"B","display_order":"11A4A20","ename":"▶","code":"0A402"},
                {"id":69,"kname":"▶기계시스템공학부","up":"A1440","div":"B","display_order":"11A4A30","ename":"▶","code":"0A403"},
                {"id":70,"kname":"건축공학과(계약학과)","up":"A2440","div":"B","display_order":"12A4410","ename":"Department of Architectural Engineering","code":"82002"},
                {"id":71,"kname":"건축안전공학과(계약학과)","up":"A2440","div":"B","display_order":"12A4420","ename":"Department of Architectural Safety Engineering","code":"82003"},
                {"id":72,"kname":"▶교직학부","up":"A4216","div":"B","display_order":"13A0110","ename":"▶Division of Teacher Education","code":"0419E"},
                {"id":73,"kname":"▶K-WITH 융합교육원","up":"A4455","div":"B","display_order":"13A0511","ename":"▶","code":"C4455"},
                {"id":74,"kname":"관광경영학과","up":"A4460","div":"B","display_order":"13A5110","ename":"Department of Tourism Management","code":"84004"},
                {"id":75,"kname":"관광개발학과","up":"A4460","div":"B","display_order":"13A5120","ename":"Department of Tourism ＆ Recreation","code":"84015"},
                {"id":76,"kname":"호텔경영학과","up":"A4460","div":"B","display_order":"13A5130","ename":"Department of Hotel ＆ Restaurant Management","code":"84005"},
                {"id":77,"kname":"외식ㆍ조리학과","up":"A4460","div":"B","display_order":"13A5140","ename":"Department of Foodservice & Culinary Management","code":"84016"},
                {"id":78,"kname":"관광이벤트학과","up":"A4460","div":"B","display_order":"13A5150","ename":"Department of Events Management","code":"84017"},
                {"id":79,"kname":"연기학과","up":"A4460","div":"B","display_order":"13A5210","ename":"Department of Acting","code":"84006"},
                {"id":80,"kname":"애니메이션영상학과","up":"A4460","div":"B","display_order":"13A5220","ename":"Department of Animation","code":"84012"},
                {"id":81,"kname":"애니메이션학과","up":"A4460","div":"B","display_order":"13A5221","ename":"애니메이션학과","code":"84008"},
                {"id":82,"kname":"실용음악학과","up":"A4460","div":"B","display_order":"13A5231","ename":"","code":"84019"},
                {"id":83,"kname":"미디어영상학과","up":"A4460","div":"B","display_order":"13A5240","ename":"Department of Media and Visual Arts","code":"84018"},
                {"id":84,"kname":"▶관광학부","up":"A4460","div":"B","display_order":"13A5A10","ename":"▶","code":"0C601"},
                {"id":85,"kname":"교육학전공","up":"0019E","div":"C","display_order":"11A0210","ename":"Education","code":"08193"},
                {"id":86,"kname":"독어독문전공","up":"0A220","div":"C","display_order":"11A1310","ename":"Major of German Language & Literature","code":"80103"},
                {"id":87,"kname":"프랑스어문전공","up":"0A220","div":"C","display_order":"11A1320","ename":"Major of French Language & Literature","code":"81002"},
                {"id":88,"kname":"일어일문전공","up":"0A220","div":"C","display_order":"11A1330","ename":"Major of Japanese Language & Literature","code":"80105"},
                {"id":89,"kname":"러시아어문전공","up":"0A220","div":"C","display_order":"11A1340","ename":"Major of Russian Language & Literature","code":"80109"},
                {"id":90,"kname":"시각정보디자인전공","up":"0A240","div":"C","display_order":"11A1510","ename":"Major of Visual Communication Design","code":"81051"},
                {"id":91,"kname":"산업디자인전공","up":"0A240","div":"C","display_order":"11A1520","ename":"Major of Industrial Design","code":"81050"},
                {"id":92,"kname":"장신구ㆍ금속디자인전공","up":"0A240","div":"C","display_order":"11A1530","ename":"Major of Jewelry & Metal Design","code":"81052"},
                {"id":93,"kname":"스포츠건강과학전공","up":"0A250","div":"C","display_order":"11A1610","ename":"Major of Sports and Health Science","code":"80702"},
                {"id":94,"kname":"레저스포츠전공","up":"0A250","div":"C","display_order":"11A1620","ename":"Major of Leisure Sport Studies","code":"81038"},
                {"id":95,"kname":"스포츠산업경영전공","up":"0A250","div":"C","display_order":"11A1630","ename":"Major of Sport Industry Management","code":"81032"},
                {"id":96,"kname":"스포츠레저산업전공","up":"0A250","div":"C","display_order":"11A1660","ename":"","code":"81033"},
                {"id":97,"kname":"사회복지전공","up":"0A320","div":"C","display_order":"11A2210","ename":"Major of Social Welfare","code":"80203"},
                {"id":98,"kname":"교정보호전공","up":"0A320","div":"C","display_order":"11A2220","ename":"Major of Corrections","code":"81003"},
                {"id":99,"kname":"청소년전공","up":"0A320","div":"C","display_order":"11A2230","ename":"Major of Youth Studies","code":"81005"},
                {"id":100,"kname":"경제전공","up":"0A340","div":"C","display_order":"11A2410","ename":"Major of Economics","code":"80301"},
                {"id":101,"kname":"응용통계전공","up":"0A340","div":"C","display_order":"11A2420","ename":"Major of Applied Statistics","code":"80305"},
                {"id":102,"kname":"경영정보전공","up":"0A360","div":"C","display_order":"11A2710","ename":"Major of Management Information Systems","code":"80306"},
                {"id":103,"kname":"회계세무전공","up":"0A360","div":"C","display_order":"11A2720","ename":"Major of Accounting & Tax","code":"81008"},
                {"id":104,"kname":"관광스포츠산업융합전공","up":"C1455","div":"C","display_order":"11A2B06","ename":"Sport Tourism Industry Interdisciplinary Major","code":"00123"},
                {"id":105,"kname":"창업융합전공","up":"C1455","div":"C","display_order":"11A2B07","ename":"Entrepreneurship Interdisciplinary Major","code":"90913"},
                {"id":106,"kname":"융합데이터공학전공","up":"C1455","div":"C","display_order":"11A2B09","ename":"Data Convergence Engineering Major","code":"90946"},
                {"id":107,"kname":"커뮤니티안전회복융합전공","up":"C1455","div":"C","display_order":"11A2B14","ename":"Interdisciplinary Study of Community Safety and Restoration","code":"90945"},
                {"id":108,"kname":"디자인비즈융합전공","up":"C1455","div":"C","display_order":"11A2B15","ename":"Design Business Interdisciplinary Major","code":"90947"},
                {"id":109,"kname":"컴퓨터공학전공","up":"0A551","div":"C","display_order":"11A2BA1","ename":"컴퓨터공학전공","code":"85511"},
                {"id":110,"kname":"인공지능전공","up":"0A551","div":"C","display_order":"11A2BA2","ename":"인공지능전공","code":"85512"},
                {"id":111,"kname":"산업경영공학전공","up":"0A552","div":"C","display_order":"11A2BB1","ename":"산업경영공학전공","code":"85521"},
                {"id":112,"kname":"경영정보전공","up":"0A552","div":"C","display_order":"11A2BB2","ename":"경영정보전공","code":"85522"},
                {"id":113,"kname":"생명과학전공","up":"0A520","div":"C","display_order":"11A3210","ename":"Major of Life Science","code":"81015"},
                {"id":114,"kname":"식품생물공학전공","up":"0A520","div":"C","display_order":"11A3220","ename":"Major of Food Science ＆ Biotechnology","code":"81016"},
                {"id":115,"kname":"교육학전공","up":"0419E","div":"C","display_order":"13A0120","ename":"Education","code":"04193"},
                {"id":116,"kname":"미디어융합콘텐츠전공","up":"C4455","div":"C","display_order":"13A0512","ename":"미디어융합콘텐츠전공","code":"90955"}
                ]
        }

function itemChange(o){

    var major_data = major.rows;
    var division = String.fromCharCode((o.id.charCodeAt()+1));
    var parent_value = o.value;

    var _init_data = '00000';
    var _init_msg = '선택하세요';
    var _no_data_msg = '데이터가 존재하지 않습니다';
    var _html = "<option value=\""+_init_data+"\" selected \>"+_init_msg+"</option>";

    if (o.id == 'A'){
        $('#B').empty();
        $('#B').append(_html);
        $('#C').empty();
        $('#C').append(_html);
    } else if(o.id == 'B'){
        $('#C').empty();
        $('#C').append(_html);
    }

    _html = "";

    if (major_data.length > 0 ){
        for(var i=0; i<major_data.length; i++){
            if(major_data[i].div == division && major_data[i].up == parent_value){
                _html += "<option value=\""+major_data[i].code+"\" \>"+major_data[i].kname+"</option>";
            }
        }
    } else {
        _html += "<option value=\""+_init_data+"\" selected \>"+_no_data_msg+"</option>";
    }
    $("#"+division).append(_html);
    var selected_value = $('#B option:selected').text()
    if (!selected_value.includes('선택') && !selected_value.includes('▶') && $('#C option').length == 1){
        $('#C option').remove();
        $('#C').attr('disabled', '');
    } else {
        $('#C').removeAttr('disabled')
    }
}