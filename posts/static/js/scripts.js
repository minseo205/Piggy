// function search_enter(e) {
//     if (e.keyCode == 13) {
//         $("#kw").val($(".kw").val());
//         // $("#page").val(1);
//         $("#searchForm").submit();
//     }
// }

// const page_elements = document.getElementsByClassName("page-link");
// Array.from(page_elements).forEach(function(element) {
//     element.addEventListener('click', function() {
//         // document.getElementById('page').value = this.dataset.page;
//         document.getElementById('searchForm').submit();
//     });
// });

const btn_search = document.getElementById("btn_search");
btn_search.addEventListener('click', function() {
    document.getElementById('kw').value = document.getElementById('search_kw').value;
    // document.getElementById('kw_age').value = document.getElementById('search_kw_age').value;
    // document.getElementById('page').value = 1;  // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
    document.getElementById('searchForm').submit();
});



