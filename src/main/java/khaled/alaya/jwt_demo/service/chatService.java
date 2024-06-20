package khaled.alaya.jwt_demo.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import khaled.alaya.jwt_demo.model.chat;
import khaled.alaya.jwt_demo.model.chatRequest;
import khaled.alaya.jwt_demo.model.user;
import khaled.alaya.jwt_demo.repo.chatRepo;
import khaled.alaya.jwt_demo.repo.userRepo;

@Service
public class chatService {


    private chatRepo chatRepo;
    private userRepo UserRepo;

    public chatService(khaled.alaya.jwt_demo.repo.chatRepo chatRepo,userRepo UserRepo) {
        this.chatRepo = chatRepo;
        this.UserRepo=UserRepo;
    }

    public chat addChat(chatRequest chat,String user){
        chat newChat = new chat(chat.chatTitle());
        List<user>users= new ArrayList();
        users.add(UserRepo.findByusername(user).get());
        users.add(UserRepo.findById(1L).get());
        newChat.setUser_id(users);
        return chatRepo.save(newChat);
    }


    public List<chat> getAllChat(String user){
        return chatRepo.findChatsByUserId(UserRepo.findByusername(user).get().getId());
    }

    public chat getChat(chat chat){
        return chatRepo.findById(chat.getId()).get();
    }

}
