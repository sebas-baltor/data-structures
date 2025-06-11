const example = [8, 5, 6, 7, 5, 6, 6, 7, 8, 12]


function MergeSort(arr){
    if(arr.length <= 1) return arr

    const middle = Math.floor(arr.length / 2)
    const left = MergeSort(arr.slice(0,middle));
    const right = MergeSort(arr.slice(middle));

    return Merge(left,right)
}

function Merge(left,right){
    let joined = []
    let i=0,j = 0

    while (i<left.length && j <right.length){
        if (left[i]<= right[j]){
            joined.push(left[i])
            i++
        }else{
            joined.push(right[j])
            j++
        }

    }
    joined.concat(left.slice(i))
    joined.concat(right.slice(j))

    return joined
}

let res = MergeSort(example)
console.log(res)
console.log("hola")