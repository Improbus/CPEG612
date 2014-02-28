function list = iSort(a)
    
    for i = (2:numel(a))
        
        compVal = a(i);
        
        counter = i - 1;

        while (counter >= 1) && (a(counter) > compVal)
            a(counter+1) = list(counter);
            counter = counter - 1;
        end

        list(counter+1)=compVal;
    end
end
    
