%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% This code is used for the segmentation of the sEMG signals in the dataset titled                %%%
%%% "Dataset for multi-channel surface electromyography (sEMG) signals of hand gestures"            %%%                                                            
%%% Mendeley Repository: http://dx.doi.org/10.17632/ckwc76xr2z.2                                    %%%
%%%                                                                                                 %%%
%%% Written by Mehmet Akif Ozdemir.                                                                 %%%
%%% Izmir Katip Celebi University                                                                   %%%
%%% Department of Biomedical Engineering                                                            %%%
%%% makif.ozdemir@ikcu.edu.tr                                                                       %%%
%%% 21/12/2021                                                                                      %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear all
close all
clc


fs = 2000; % sampling rate "Hz"

%% DESIRED sEMG SEGMENTS LENGTH as second
signal_segment_starting=0; % indicate the desired beginning of segment as sec (usually 0 or 1)
signal_segment_ending=6; %indicate the desired ending of segment as sec (usually 5 or 6)
%ATTENTION: signal_segment_long=signal_segment_ending-signal_segment_starting; % max segment long is 6
%if you want to use sEMG segments which gestures are not beginning you can change the signal_segment_starting like -1

%% Get sEMG Records directory:
current_folder= '..\sEMG_HandGesture_Study'; %  !!!change with current folder!!!
addpath(genpath(current_folder))
Base  = strcat(current_folder,'\sEMG-dataset\filtered\mat'); % filtered recommended, change with raw or filtered
List  = dir(fullfile(Base, '**', '*.mat'));
Files = fullfile({List.folder}, {List.name});
Nd = cellfun( @str2double, regexp(Files, '\d+', 'match') );
[~,I] = sort(Nd);
Files = Files(I);

%%Using for automated segmentation of all participant sEMG data to sEMG gesture segment.
for iFile = 1:numel(Files) %40 participants, each sEMG data channel consist 1280000=640 sec* 2000 fs data point

    load(Files{iFile}) % load .. sEMG data of participants
    % Each File consists of : "data"        : discrete 4 ch sEMG signals
    %                         "fs"          : sampling rate as "2000"
    %                         "iD"          : participant iD as " 1 to 40"
    %                         "isi"         : sampling interval as "0.5"
    %                         "isi_units"   : sampling interval unit as "ms"
    %                         "labels"      : current channels' labels
    %                         "start_sample": start time of the signal recording as "0"
    %                         "units"       : sEMG data units as "mV"


    for rep=0:4 % 5 repetition, one cycle took 104 sec + 30 sec resting time, total 134 second fifth cycye only took 104 sec

        if rep==0
            rep_coeff=4; % first cycle: first REST start at fourth second and this cycle took 134 sec
        elseif rep==1
            rep_coeff=138; % second cycle: REST start at 138 sec= 104 sec (first cycle) + 30 sec (long rest) + 4 sec (begening rest)
        elseif rep==2
            rep_coeff=272; % third cycle: REST start at 272 sec= 268 sec (first two cycles) + 4 sec (begening rest)
        elseif rep==3
            rep_coeff=406; % fourth cycle: REST start at 406 sec= 402 sec (first three cycles) + 4 sec (begening rest)
        elseif rep==4
            rep_coeff=540; % fifth cycle: REST start at 540 sec= 536 sec (first four cycles) + 4 sec (begening rest)
        end % end is 640 sec


        for gesture =0:9 % a total of 10 hand gesture
            %0: X = REST
            %1: E = EXTENSION
            %2: F = FLEXION
            %3: U = ULNAR DEVIATION
            %4: R = RADIAL DEVIATION
            %5: G = GRIP
            %6: B = ABDUCTION
            %7: D = ADDUCTION
            %8: S = SUPINATION
            %9: P = PRONATION

            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            %%%USE THE CODE BELOW FOR YOUR MULTI-CHANNEL ANALYSIS%%%
            multi_channel_sEMG_data=data((signal_segment_starting+rep_coeff+(gesture*10))*fs+1:...
                ((rep_coeff+(gesture*10))+signal_segment_ending)*fs,:);
            % It provides 6 seconds sEMG data of a single gesture belonging to 4-channel sEMG data.


            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %%%                 USE HERE "multi_channel_sEMG_data" TO ANALYZE               %%%                                                                      %%
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


            switch gesture
                case 0%0: X = REST
                    %% Do something in here for REST segment i.e. save the multi-channel signal segment or
                    % make the multivariate anaylsis of the multi-channel segment, etc.
                    % Rest_signal_multiCH=multi_channel_sEMG_data;
                    % Example= plot(Rest_signal_multiCH);
                case 1%1: E = EXTENSION

                case 2%2: F = FLEXION

                case 3%3: U = ULNAR DEVIATION

                case 4%4: R = RADIAL DEVIATION

                case 5%5: G = GRIP

                case 6%6: B = ABDUCTION

                case 7%7: D = ADDUCTION

                case 8%8: S = SUPINATION

                case 9%9: P = PRONATION

            end %gesture swtich

            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            %%%USE THE CODE BELOW FOR YOUR CHANNEL BASED ANALYSIS%%%
            for channel=1:4 % 4 ch sEMG data
                single_channel_sEMG_data=data((signal_segment_starting+rep_coeff+(gesture*10))*fs+1:...
                    ((rep_coeff+(gesture*10))+signal_segment_ending)*fs,channel);
                % The above code lines loops through all the repetitions, all the channels,
                % and all the gestures of all the participants, respectively, with the for loops.
                % It provides 6 seconds sEMG data of a single gesture belonging to a single channel.


                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                %%%                 USE HERE "single_channel_sEMG_data" TO ANALYZE              %%%                                                                      %%
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


                switch gesture
                    case 0%0: X = REST
                        %% Do something in here for REST segment i.e. save the single-channel signal segment or
                        % take the STFT of the single-channel segment, etc.
                        % Rest_signal_singleCH=single_channel_sEMG_data;
                        % Example= plot(Rest_signal_singleCH);
                    case 1%1: E = EXTENSION

                    case 2%2: F = FLEXION

                    case 3%3: U = ULNAR DEVIATION

                    case 4%4: R = RADIAL DEVIATION

                    case 5%5: G = GRIP

                    case 6%6: B = ABDUCTION

                    case 7%7: D = ADDUCTION

                    case 8%8: S = SUPINATION

                    case 9%9: P = PRONATION

                end %gesture swtich
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            end%channel for

        end%gesture for

    end%repetition for

end%participants for