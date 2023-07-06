use std::fs;

fn main() {
    let content = get_content();

    let mut max = 0;
    let mut group = 0;

    for line in content.lines(){
        if line.len() > 0 {
            group += line.parse::<i32>().expect("Input will be number!");
        } else {
            if max < group {
                max = group;
            }
            group = 0;
        }
    }

    println!("The result is {}", max);
}


fn get_content() -> String {
    let content = match fs::read_to_string("../../input/day1"){
        Ok(data) => data,
        Err(_) => panic!("Couldn't read the data for day1"),
    };

    content
}
