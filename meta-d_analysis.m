clear all
close all
%specify files to analyse
%These files need to be obtained from the .csv output of the psychopy experiment. 
%They will have respective prolific IDs and need to be uplaoded in matlab before one is able to analyse them with this script.
%ALSO(!) Jags 3.4.0 needs to be downloaded on your machine and ideally saved in the same working directory than matlab and the files you are working with.
filecode{1} = '5d41925ef7b99500012b960e_motion_arrcues_09_12_2022-02-07_13h18.41.640';
filecode{2} = '5e66cb6046fdb7455e9d480d_motion_arrcues_09_12_2022-02-07_12h23.09.177';
filecode{3} = '5fd65eb179363c54f7e0ab96_EF_10_07_motion_arrcues_09_12_2022-02-07_12h08.26.815';
filecode{4} = '59be90270ac77f0001f059e6_motion_arrcues_09_12_2022-02-07_12h20.01.320';
filecode{5} = '60c212bd1d3721d909c0580d_motion_arrcues_09_12_2022-02-07_12h43.50.434';
filecode{6} = '615c500bec9a6a7c10c6c12b_motion_arrcues_09_12_2022-02-07_12h26.31.919';
filecode{7} = '60804e82d6a80b97ba658e17_motion_arrcues_09_12_2022-02-07_12h13.01.303';
filecode{8} = '5801275ab80310000163f0f8_motion_arrcues_09_12_2022-02-07_12h22.51.792';
filecode{9} = 'Prolific_ID_or_uniqu5c609e77044f100001a4bcc7e_code_initials__birthday_motion_arrcues_09_12_2022-02-07_12h41.51.537';
filecode{10} = 'Prolific_ID_or_unique_code_initials__birthday_motion_arrcues_09_12_2022-02-07_12h42.34.377'; %5efe07a08ce2d32bb2c5a1fd
filecode{11} = 'Prolific_ID_or_unique_code_initials__birthday_motion_arrcues_09_12_2022-02-07_13h07.08.288'; %5ced352a6b2b3d001a94c003
for sub = 1:length(filecode)
    clearvars -except filecode sub results
%load csv into matlab
file = filecode{sub}
file_open = strcat(file,'.csv');
tbl = readtable(file_open);

%lift variables of interest
resp = tbl.key_resp_keys;
cue = tbl.cue;
direction = tbl.direction;

for a=12:412
    %determine whether outcome was expected or unexpected based on arrow
    if direction(a)==1 && cue(a)==1 || direction(a)==-1 && cue(a)==-1
        expectation(a)=1; %expected
    elseif direction(a)==1 && cue(a)==-1 || direction(a)==-1 && cue(a)==1
        expectation(a)=2;%unexpected
    end
end

%S1 = -1 (left), S2 = 1 (right)
%initialise as empty
nR_S1_exp = [0 0 0 0];
nR_S2_exp = [0 0 0 0];
nR_S1_unexp = [0 0 0 0];
nR_S2_unexp = [0 0 0 0];

for a=12:412
    if resp(a)>0
    if direction(a) ==-1 %S1
        if expectation(a)==1 
            nR_S1_exp(resp(a))=nR_S1_exp(resp(a))+1;
        elseif expectation(a)==2
            nR_S1_unexp(resp(a))=nR_S1_unexp(resp(a))+1;
        end
    elseif direction(a) == 1 %S2
        if expectation(a)==1
            nR_S2_exp(resp(a))=nR_S2_exp(resp(a))+1;
        elseif expectation(a)==2
            nR_S2_unexp(resp(a))=nR_S2_unexp(resp(a))+1;
        end
    end
    end


end
    exp_fit = fit_meta_d_mcmc(nR_S1_exp,nR_S2_exp);
    unexp_fit = fit_meta_d_mcmc(nR_S1_unexp,nR_S2_unexp);
    total = sum(nR_S1_exp) + sum(nR_S2_exp) + sum(nR_S1_unexp) + sum(nR_S2_unexp);
    %store vars for analysis
    results(sub,1:8) = [sub total exp_fit.d1 unexp_fit.d1 exp_fit.meta_d unexp_fit.meta_d exp_fit.M_ratio unexp_fit.M_ratio];
end


