let previewContainer = document.querySelector('.program-preview');
let previewBox = previewContainer.querySelectorAll('.preview');

document.querySelectorAll('.program-container .program').forEach(program =>{
    program.onclick = () =>{
        previewContainer.style.display = 'flex';
        let name = program.getAttribute('data-name');
        previewBox.forEach(preview =>{
            let target = preview.getAttribute('data-target');
            if(name == target){
                preview.classList.add('active');
            }
        });
    };
});

previewBox.forEach(close =>{
    close.querySelector('.fa-times').onclick = () =>{
        close.classList.remove('active');
        previewContainer.style.display = 'none';
    };
});